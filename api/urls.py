from django.urls import path
from .views import CategoryView , ShowCategory , CategoryCount 
from .views import ProductView  , ProductCount , CategoryProducts , ShowProduct
from .views import InfoView , ShowInfo
urlpatterns = [
	path('categories/' , CategoryView.as_view() , name="categories"),
	path('categories/<int:pk>' , CategoryView.as_view() , name="updateORshowORdelete"),
	path('categories/<int:pk>/show' , ShowCategory.as_view() , name="show_category"),
	path('categories/count' , CategoryCount.as_view() , name="categories_count"),
	path('category/<int:pk>/products' , CategoryProducts.as_view() , name="all_category_products"),
	path('products/' , ProductView.as_view() , name="products"),
	path('products/<int:pk>' , ProductView.as_view() , name="updateORshowORdelete"),
	path('products/<int:pk>/show' , ShowProduct.as_view() , name="show_Product"),
	path('products/count' , ProductCount.as_view() , name="products_count"),
	path('info/' , InfoView.as_view() , name="info"),
	path('info/<int:pk>' , InfoView.as_view() , name="updateORshowORdelete"),
	path('info/<int:pk>/show' , ShowInfo.as_view() , name="show_info"),
]
