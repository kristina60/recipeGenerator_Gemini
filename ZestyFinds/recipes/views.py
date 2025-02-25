from django.shortcuts import render, redirect
from django.views import View
from google.cloud import aiplatform
from google import genai
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the AI client with your actual API key
client = genai.Client(api_key=os.getenv('GEMINI_API_KEYS'), http_options={'api_version': 'v1alpha'}) 

# @method_decorator(login_required(login_url='/authentication/login'), name='dispatch')
# @method_decorator(never_cache, name='dispatch')
class IngredientsInputView(View):
    def get(self, request):
        # Render the input form
        return render(request, 'recipes/ingredients_input.html')

    def post(self, request):
        ingredients = request.POST.get('ingredients', '')
        time_limit = request.POST.get('time', '')
        serving = request.POST.get('serving', '')
        cooking_Method=request.POST.get('cookingMethod','')
        
        
        # Save data in session
        request.session['ingredients'] = ingredients
        request.session['time_limit'] = time_limit
        request.session['serving'] = serving
        request.session['cooking_Method'] = cooking_Method

        prompt = f"List the names of food recipes that can be made using the {ingredients} within {time_limit} minutes, and serve {serving} people. The recipes should be prepared using the {cooking_Method}. . Give only the names of the recipes as output."

        try:
            response = client.models.generate_content(model='gemini-2.0-flash-thinking-exp', contents=[prompt])
            print("Response:", response) #debug

            # Extract recipe names from the response
            recipe_list = []
            if response and response.candidates:
                for candidate in response.candidates:
                    if candidate.content and candidate.content.parts:
                        for part in candidate.content.parts:
                            if part.text:
                                # Split multiline text into individual recipes and clean it
                                recipes = part.text.strip().split('\n')
                                recipe_list.extend([recipe.strip() for recipe in recipes if recipe.strip()])
            else:
                recipe_list = ["No recipes found."]  # Default message if no candidates are found

        except Exception as e:
            print(f"Error during API call: {e}")
            recipe_list = ["Error fetching recipes. Please try again."]

        # Render the recipes as a list
        return render(request, 'recipes/ingredients_list.html', {'recipe_list': recipe_list})


import re 


class RecipeInstructionsView(View):
    def get(self, request, recipe_name):
        # Retrieve data from session
        ingredients = request.session.get('ingredients', '')
        time_limit = request.session.get('time_limit', '')
        serving = request.session.get('serving', '')
        cooking_Method = request.session.get('cooking_Method', '')
        print(ingredients)
        prompt = f"Provide detailed step-by-step instructions to prepare the recipe: {recipe_name}, using only the following ingredients: {ingredients}. The recipe should serve {serving} people, take no more than {time_limit} minutes to cook, and be prepared using {cooking_Method}. If there are any additional ingredients required, please highlight them clearly."

        # Default instructions message
        instructions = "Instructions not found."

        try:
            # Call the content generation API (or other data source)
            response = client.models.generate_content(model='gemini-2.0-flash-thinking-exp', contents=[prompt])

            # Process the API response
            if response and response.candidates:
                raw_instructions = "\n\n".join(
                    part.text for part in response.candidates[0].content.parts if getattr(part, "text", None)
                )

                # # Add line breaks before numbers (e.g., 1., 2., 3.) using regex
                # formatted_instructions = re.sub(r'(?<=\b)(\d+\.)', r'\n\1', raw_instructions).strip()
                # instructions = formatted_instructions
                  # Clean the raw instructions
                 # Remove unwanted sequences
                cleaned_instructions = re.sub(r'[#!*]', '', raw_instructions)  # Remove #, *, or !
                cleaned_instructions = re.sub(r'(?<=\b)(\d+\.)', r'\n\1', cleaned_instructions)  # Add line breaks
                instructions = cleaned_instructions.strip()  # Trim leading and trailing whitespace
        except Exception as e:
            print(f"Error during API call: {e}")

        # Render the template with the recipe name and instructions
        return render(request, 'recipes/recipe_instructions.html', {
            'recipe_name': recipe_name,
            'instructions': instructions
        })



