from django.contrib import admin
from django.utils.html import format_html
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    fields = ('image', 'caption', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; border-radius: 5px;">', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_with_preview', 'date', 'post_actions')
    list_display_links = ('title_with_preview',)
    search_fields = ('title', 'description')
    readonly_fields = ('image_preview',)
    inlines = [PostImageInline]
    save_on_top = True
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'description'),
            'classes': ('wide',)
        }),
        ('Media', {
            'fields': ('image', 'image_preview'),
            'classes': ('collapse',)
        }),
        ('Publication', {
            'fields': ('date',),
            'classes': ('wide',)
        }),
    )

    def title_with_preview(self, obj):
        if obj.image:
            return format_html(
                '<div style="display: flex; align-items: center; gap: 10px;">'
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;">'
                '<span>{}</span>'
                '</div>',
                obj.image.url, obj.title
            )
        return obj.title
    title_with_preview.short_description = 'Title'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">',
                obj.image.url
            )
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'

    def post_actions(self, obj):
        return format_html(
            '<a class="button" href="/admin/blog/post/{}/change/" style="margin-right: 5px;">Edit</a>'
            '<a class="button" href="/admin/blog/post/{}/delete/" style="background: #ba2121;">Delete</a>',
            obj.id, obj.id
        )
    post_actions.short_description = 'Actions'

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
