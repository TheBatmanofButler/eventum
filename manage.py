from sys import argv, exit
from script import backfill_blog, import_images, generate_email

def print_usage():
    print "Usage:"
    print "%s --backfill-blog (-b) Backfill blog posts from data/jekyll-posts" % argv[0]
    print "%s --import-images (-i) Import images from data/jekyll-images" % argv[0]
    print "%s --generate-email (-e) Generate email containing event information" % argv[0]

if __name__ == '__main__':
    if '--backfill-blog' in argv or '-b' in argv:
        backfill_blog.backfill_from_jekyll('data/old-website-data/posts')
    elif '--import-images' in argv or '-i' in argv:
        import_images.import_from_directory('data/jekyll-images')
    elif '--generate-email' in argv or '-e' in argv:
        generate_email.generate_events_email()