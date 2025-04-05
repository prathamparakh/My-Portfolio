# Personal Portfolio Website

A modern, responsive personal portfolio website built with React and Tailwind CSS.

## Overview

This portfolio website showcases professional experience, skills, education, and projects in a clean, interactive interface. The website features smooth scrolling navigation, responsive design, and interactive elements to engage visitors.

## Features

- **Responsive Design**: Fully responsive layout that works on mobile, tablet, and desktop devices
- **Modern UI**: Clean interface built with Tailwind CSS
- **Interactive Navigation**: Smooth scrolling to different sections
- **Project Showcase**: Displays technical projects with descriptions and links to GitHub repositories
- **Contact Form**: Integrated contact form for visitor inquiries
- **Social Links**: Easy access to LinkedIn and GitHub profiles

## Sections

1. **Home**: Introduction with quick access buttons
2. **About**: Personal bio, contact information, and education background
3. **Experience**: Professional work experience and leadership roles
4. **Projects**: Technical project showcase with GitHub repository links
5. **Skills**: Technical skills and certifications
6. **Contact**: Contact form and information

## Technologies Used

- **React**: Frontend library for building the user interface
- **Tailwind CSS**: Utility-first CSS framework for styling
- **JavaScript**: Programming language for interactivity
- **GitHub Pages**: For hosting the portfolio website

## Project Structure

```
personal-portfolio/
├── public/
│   ├── assets/
│   │   └── image/
│   │       └── profile.jpeg
│   └── Resume__Pratham_datascience_student.pdf.pdf
├── src/
│   ├── App.js
│   ├── ProjectsSection.js
│   ├── index.js
│   └── ...
└── package.json
```

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/prathamparakh/personal-portfolio.git
   cd personal-portfolio
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

4. Build for production:
   ```
   npm run build
   ```

## Customization

### Personal Information
Update the `personalInfo` object in `App.js` to change your name, contact details, and social media links.

### Experience and Education
Modify the `experience`, `education`, and `leadership` arrays in `App.js` to reflect your background.

### Projects
Edit the `projects` array in `ProjectsSection.js` to showcase your own projects with descriptions and repository links.

### Skills
Adjust the `skills` object in `App.js` to highlight your technical skills and languages.

## Deployment

This portfolio can be deployed to GitHub Pages:

1. Install the gh-pages package:
   ```
   npm install --save gh-pages
   ```

2. Add the following to your `package.json`:
   ```json
   "homepage": "https://prathamparakh.github.io/personal-portfolio",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```

3. Deploy the site:
   ```
   npm run deploy
   ```

## License

This project is open source and available under the MIT License.

## Credits

Developed by Pratham Parakh.

---

Feel free to fork this project and customize it for your own portfolio!
