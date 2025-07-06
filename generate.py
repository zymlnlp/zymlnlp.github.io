import os
import markdown

POSTS_DIR = 'posts'
TEMPLATES_DIR = 'templates'
STATIC_DIR = 'static'

with open(os.path.join(TEMPLATES_DIR, 'post_template.html')) as f:
    POST_TEMPLATE = f.read()
with open(os.path.join(TEMPLATES_DIR, 'index_template.html')) as f:
    INDEX_TEMPLATE = f.read()

post_entries = []

for filename in os.listdir(POSTS_DIR):
    if not filename.endswith('.md'):
        continue
    path = os.path.join(POSTS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html = markdown.markdown(md_text, extensions=["extra"])
    title = 'Untitled'
    for line in md_text.splitlines():
        if line.startswith('# '):
            title = line[2:].strip()
            break
    slug = os.path.splitext(filename)[0]
    output_path = os.path.join(POSTS_DIR, f'{slug}.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(POST_TEMPLATE.format(title=title, content=html))
    post_entries.append(f'<li><a href="posts/{slug}.html">{title}</a></li>')

index_html = INDEX_TEMPLATE.format(posts='\n      '.join(sorted(post_entries)))
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('Generated site with', len(post_entries), 'posts.')
