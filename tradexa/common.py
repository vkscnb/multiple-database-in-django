from user.models import Post
from product.models import Product

def post_and_product_list(request):

    post_data = Post.objects.filter(user=request.user.id).order_by('-created_at')
    product = Product.objects.all().order_by('-created_at')

    return {'user_post_data':list(post_data), 'all_product_data':list(product)}