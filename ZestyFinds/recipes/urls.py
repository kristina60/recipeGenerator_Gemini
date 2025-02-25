# from django.urls import path
# from .views import AddIngredients

# urlpatterns = [
#     path("add-ingredients/", AddIngredients.as_view(), name="add_ingredients"),
# ]
from django.urls import path
from .views import IngredientsInputView,RecipeInstructionsView

# urlpatterns = [
#      path('add-ingredients/', IngredientsInputView.as_view(), name='add_ingredients'),
    
# ]
urlpatterns = [
    
     path("", IngredientsInputView.as_view(), name="add_ingredients"),
     path("recipe/<str:recipe_name>/", RecipeInstructionsView.as_view(), name="recipe_instructions"),
 ]
