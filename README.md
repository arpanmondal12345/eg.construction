# Excellent Great Construction — HTML Website

Plain HTML + CSS + JavaScript. No build step: upload this folder as it is.

```
index.html      the whole page (all text and section layout)
css/style.css   all styles
js/script.js    menu, project gallery + lightbox, contact form, phone/WhatsApp/Instagram settings
images/         photos (each in 720, 1440 and 2400 px WebP)
favicon.svg     browser tab icon
og-image.jpg    preview image when the link is shared on WhatsApp/Facebook
```

## Put it live on GitHub Pages
Open a terminal in this folder and run:
```
git init
git add .
git commit -m "Website"
git branch -M main
git remote add origin https://github.com/arpanmondal12345/eg.construction.git
git push -u origin main
```
Then on GitHub: Settings → Pages → Deploy from a branch → main / (root) → Save.

## Editing
- **Text:** edit it directly in `index.html`.
- **Phone, WhatsApp, Instagram:** change them at the top of `js/script.js`, and also search-and-replace
  `8764345647` and `eg.construction` in `index.html`.
- **Project gallery:** add or remove photos in the `PROJECTS` list in `js/script.js`.
- **Contact form:** it opens WhatsApp with the visitor's details. To also get emails, paste a free
  Formspree endpoint into `FORM_ENDPOINT` in `js/script.js`.

## Note on styles
`css/style.css` was generated with Tailwind CSS and only contains the classes already used on the page.
Changing text, links and images is safe. If you add new Tailwind class names that aren't on the page yet,
they won't have any style until the CSS is regenerated.
