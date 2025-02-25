Recipe Generator Using Gemini API

Description
This Django-based AI-powered recipe generator utilizes the **Gemini API** to suggest recipes based on user inputs. Users can:
- Add ingredients
- Specify the number of servings
- Set cooking time and method
- Get a list of AI-generated recipes
- Select a recipe to view full instructions

Features
- AI-generated recipe recommendations
- User-friendly input for ingredients, servings, time, and method
- Detailed step-by-step cooking instructions
- Built with Django for backend processing

Installation
1. Clone the repository:
   bash
   git clone https://github.com/kristina60/recipeGenerator_Gemini.git
   cd recipeGenerator_Gemini
   
2. Create a virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   
3. Install dependencies:
   bash
   pip install -r requirements.txt
   
4. Set up environment variables:
   - Create a `.env` file and add your Gemini API key:
     
     SECRET_KEYS=your_api_key_here
     
5. Run the Django server:
   bash
   python manage.py runserver
   

Usage
1. Open the web app in your browser.
2. Enter available ingredients, servings, cooking time, and method.
3. Receive a list of AI-generated recipes.
4. Choose a recipe to view detailed cooking instructions.

Technologies Used
- Django – Web framework
- Gemini API – AI-powered recipe generation
- HTML, CSS, bootstrap– Frontend
- SQLite – Database

License
This project is licensed under the MIT License.

Author
Developed by Kristina Basnet

# recipeGenerator_Gemini
