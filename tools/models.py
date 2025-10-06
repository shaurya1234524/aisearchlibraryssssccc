from django.db import models
from django.contrib.auth.models import User

PRICING_CHOICES = (
    ('Free', 'Free'),
    ('Premium', 'Premium'),
    ('Freemium', 'Freemium'),
)

CATEGORY_CHOICES = (
    ('AI Art', 'AI Art'),
    ('AI Tools', 'AI Tools'),
    ('App Development', 'App Development'),
    ('Automation', 'Automation'),
    ('Blockchain', 'Blockchain'),
    ('Career', 'Career'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Copywriting', 'Copywriting'),
    ('Cryptocurrency', 'Cryptocurrency'),
    ('Customer Support', 'Customer Support'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Data Analysis', 'Data Analysis'),
    ('Design', 'Design'),
    ('Deep Learning', 'Deep Learning'),
    ('E-commerce', 'E-commerce'),
    ('Education', 'Education'),
    ('Entrepreneurship', 'Entrepreneurship'),
    ('Fitness', 'Fitness'),
    ('Food & Beverages', 'Food & Beverages'),
    ('Gaming', 'Gaming'),
    ('Health', 'Health'),
    ('HR', 'HR'),
    ('Investing', 'Investing'),
    ('Legal', 'Legal'),
    ('Lifestyle', 'Lifestyle'),
    ('Machine Learning', 'Machine Learning'),
    ('Marketing', 'Marketing'),
    ('Mental Health', 'Mental Health'),
    ('Music', 'Music'),
    ('News', 'News'),
    ('Personal Finance', 'Personal Finance'),
    ('Photography', 'Photography'),
    ('Product Management', 'Product Management'),
    ('Productivity', 'Productivity'),
    ('Real Estate', 'Real Estate'),
    ('Robotics', 'Robotics'),
    ('SEO', 'SEO'),
    ('Social Media', 'Social Media'),
    ('Sports', 'Sports'),
    ('Startups', 'Startups'),
    ('Travel', 'Travel'),
    ('UI/UX', 'UI/UX'),
    ('Video Editing', 'Video Editing'),
    ('VR/AR', 'VR/AR'),
    ('Web Development', 'Web Development'),
    ('Writing', 'Writing'),
    ('IoT', 'IoT'),
    ('Networking', 'Networking'),
)


class Tool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tool_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='AI Tools')  # ✅ like pricing
    tags = models.CharField(max_length=200, blank=True)  
    pricing = models.CharField(max_length=10, choices=PRICING_CHOICES, default='Free')
    website = models.URLField(blank=True, null=True)
    upvotes = models.PositiveIntegerField(default=0)
    upvoted_by = models.ManyToManyField(User, blank=True, related_name='upvoted_tools')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
