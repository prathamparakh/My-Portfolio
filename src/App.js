import React, { useState } from 'react';

const Portfolio = () => {
  const [activeSection, setActiveSection] = useState('home');
  
  // Portfolio data based on the resume
  const personalInfo = {
    name: "Pratham Parakh",
    location: "Mumbai, India",
    phone: "+91 9082937049",
    email: "prathamparakh918@gmail.com",
    linkedin: "pratham-parakh",
    github: "prathamparakh",
    resumeFile: "/RESUME.pdf" 
  };
  
  const education = [
    {
      degree: "Bachelor of Technology in CS Engineering (Data Science)",
      institution: "Mukesh Patel School of Technology Management & Engineering, NMIMS",
      period: "2023 – 2026",
      details: "GPA: 3.65/4.0"
    },
    {
      degree: "BS in Cybersecurity & MS in Business Analytics",
      institution: "Virginia Tech",
      period: "2026 – 2028",
      details: "International partnership program"
    }
  ];
  
  const experience = [
    {
      position: "Co-founder",
      company: "NUMERO ORACLE",
      location: "Mumbai, India",
      period: "2024 – Present",
      achievements: [
        "Implemented data-driven strategies resulting in 40% increase in business performance",
        "Developed targeted social media campaigns enhancing brand outreach by 65%",
        "Established 15+ strategic partnerships with key industry stakeholders"
      ]
    },
    {
      position: "Assistant Manager",
      company: "AAYUSH COTTFABS PVT LTD",
      location: "Mumbai, India",
      period: "2021 – 2022",
      achievements: [
        "Managed operations team of 12, ensuring 95% on-time delivery and process efficiency",
        "Optimized supply chain processes, reducing operational costs by 18%",
        "Implemented digital inventory tracking system improving accuracy by 32%"
      ]
    }
  ];
  
  const projects = [
    {
      name: "NEO NET ENTERPRISE",
      year: "2025",
      details: [
        "Engineered AI-powered business toolset using Python, TensorFlow, and AWS cloud services",
        "Implemented market prediction algorithms with 89% accuracy for financial forecasting",
        "Created automated workflows reducing administrative overhead by 65% for startups"
      ]
    },
    {
      name: "PAPER TRADING PLATFORM",
      year: "2023",
      details: [
        "Architected full-stack trading simulation using C++, REST APIs, and SQL databases",
        "Integrated real-time market data processing with 99.7% uptime reliability"
      ]
    }
  ];
  
  const leadership = [
    {
      position: "Head of Sports Committee",
      organization: "MPSTME",
      location: "Mumbai, India",
      period: "2023 – Present",
      achievements: [
        "Led 35-member team organizing 12+ annual events for 3,000+ participants",
        "Secured sponsorships of 500,000, representing 40% year-over-year growth"
      ]
    }
  ];
  
  const skills = {
    languages: ["Python", "C++", "C", "Java", "SQL", "HTML/CSS", "JavaScript"],
    technologies: ["AWS","ReactJS", "MySQL", "Tableau", "Docker", "MongoDB"],
    additional: ["Data Analysis", "Project Management", "Fluent in English, Hindi, Tamil, French"]
  };
  
  const certifications = [
    {
      name: "AWS Certified Cloud Practitioner",
      year: "2023"
    },
    {
      name: "Google Data Analytics Certificate",
      year: "2022"
    }
  ];
  
  // Navigation handling
  const handleNavClick = (section) => {
    setActiveSection(section);
    // Add smooth scrolling to section
    document.getElementById(section).scrollIntoView({
      behavior: 'smooth'
    });
  };
  
  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="sticky top-0 z-10 bg-white shadow-md">
        <div className="container mx-auto px-6 py-3">
          <div className="flex items-center justify-between">
            <div className="text-xl font-bold text-gray-800">{personalInfo.name}</div>
            <div className="hidden md:flex space-x-8">
              {['home', 'about', 'experience', 'projects', 'skills', 'contact'].map((item) => (
                <button
                  key={item}
                  onClick={() => handleNavClick(item)}
                  className={`${
                    activeSection === item ? 'text-blue-600' : 'text-gray-600 hover:text-blue-500'
                  } transition-colors duration-300 text-sm uppercase font-medium`}
                >
                  {item}
                </button>
              ))}
            </div>
            
            {/* Mobile menu button */}
            <div className="md:hidden flex items-center">
              <button className="outline-none mobile-menu-button">
                <svg
                  className="w-6 h-6 text-gray-500 hover:text-blue-500"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </nav>
      
      {/* Hero Section */}
<section id="home" className="py-20 bg-gradient-to-r from-blue-500 to-blue-700 text-white">
  <div className="container mx-auto px-6 text-center">
    <h1 className="text-5xl font-bold mb-4">{personalInfo.name}</h1>
    <p className="text-xl mb-8">Data Scientist | Entrepreneur | Tech Enthusiast</p>
    <div className="flex justify-center space-x-4">
      <button
        onClick={() => handleNavClick('contact')}
        className="bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors duration-300"
      >
        Contact Me
      </button>
      <button
        onClick={() => handleNavClick('projects')}
        className="border-2 border-white text-white px-6 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition-colors duration-300"
      >
        View My Work
      </button>
      {/* Add Resume Download Button */}
      <a
        href={personalInfo.resumeFile}
        download
        className="bg-green-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors duration-300 flex items-center"
      >
        <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
        </svg>
        Download Resume
      </a>
    </div>
  </div>
</section>
      
      {/* About Section */}
      <section id="about" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">About Me</h2>
          <div className="flex flex-col md:flex-row items-center">
            <div className="md:w-1/2 mb-8 md:mb-0">
              <div className="bg-gray-300 h-64 w-64 mx-auto rounded-full overflow-hidden">
                {/* Placeholder for profile image */}
                <img src="/assets/image/profile.jpeg" alt="Profile" className="h-full w-full object-cover" />
              </div>
            </div>
            <div className="md:w-1/2">
              <div className="text-gray-600 mb-6">
                <p className="mb-4">
                  I'm a passionate tech professional with expertise in data science, cybersecurity, and business analytics. 
                  Currently pursuing my Bachelor of Technology in CS Engineering with a focus on Data Science at NMIMS.
                </p>
                <p>
                  As a co-founder of NUMERO ORACLE, I've implemented data-driven strategies that have significantly 
                  improved business performance. I combine technical expertise with leadership skills to deliver 
                  impactful solutions.
                </p>
              </div>
              <div className="grid grid-cols-2 gap-4 text-sm mb-6">
                <div>
                  <p className="font-semibold text-gray-700">Name:</p>
                  <p className="text-gray-600">{personalInfo.name}</p>
                </div>
                <div>
                  <p className="font-semibold text-gray-700">Email:</p>
                  <p className="text-gray-600">{personalInfo.email}</p>
                </div>
                <div>
                  <p className="font-semibold text-gray-700">Location:</p>
                  <p className="text-gray-600">{personalInfo.location}</p>
                </div>
                <div>
                  <p className="font-semibold text-gray-700">Phone:</p>
                  <p className="text-gray-600">{personalInfo.phone}</p>
                </div>
              </div>
              
              {/* Resume Download Button in About Section */}
              <div className="mt-4">
                <a
                  href={personalInfo.resumeFile}
                  download
                  className="bg-blue-600 text-white px-4 py-2 rounded-md font-medium hover:bg-blue-700 transition-colors duration-300 inline-flex items-center"
                >
                  <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                  </svg>
                  Download My Resume
                </a>
              </div>
            </div>
          </div>
          
          {/* Education */}
          <div className="mt-16">
            <h3 className="text-2xl font-bold text-gray-800 mb-6">Education</h3>
            <div className="space-y-8">
              {education.map((edu, index) => (
                <div key={index} className="border-l-4 border-blue-500 pl-4 py-2">
                  <p className="text-gray-500 text-sm">{edu.period}</p>
                  <h4 className="text-lg font-semibold text-gray-800">{edu.degree}</h4>
                  <p className="text-gray-600">{edu.institution}</p>
                  <p className="text-gray-600 text-sm">{edu.details}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
      
      {/* Experience Section */}
      <section id="experience" className="py-20 bg-gray-100">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">Professional Experience</h2>
          <div className="space-y-12">
            {experience.map((exp, index) => (
              <div key={index} className="bg-white rounded-lg shadow-md p-6">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                  <div>
                    <h3 className="text-xl font-bold text-gray-800">{exp.position}</h3>
                    <p className="text-gray-600">{exp.company}, {exp.location}</p>
                  </div>
                  <p className="text-blue-500 font-medium">{exp.period}</p>
                </div>
                <ul className="list-disc pl-5 space-y-2 text-gray-600">
                  {exp.achievements.map((achievement, i) => (
                    <li key={i}>{achievement}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
          
          {/* Leadership */}
          <div className="mt-16">
            <h3 className="text-2xl font-bold text-gray-800 mb-6">Leadership Experience</h3>
            <div className="space-y-8">
              {leadership.map((lead, index) => (
                <div key={index} className="bg-white rounded-lg shadow-md p-6">
                  <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                    <div>
                      <h4 className="text-xl font-bold text-gray-800">{lead.position}</h4>
                      <p className="text-gray-600">{lead.organization}, {lead.location}</p>
                    </div>
                    <p className="text-blue-500 font-medium">{lead.period}</p>
                  </div>
                  <ul className="list-disc pl-5 space-y-2 text-gray-600">
                    {lead.achievements.map((achievement, i) => (
                      <li key={i}>{achievement}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
      
      {/* Projects Section */}
      <section id="projects" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">Technical Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {projects.map((project, index) => (
              <div key={index} className="bg-white rounded-lg shadow-lg overflow-hidden">
                <div className="bg-gray-300 h-48">
                  {/* Placeholder for project image */}
                  <img src={`/api/placeholder/600/300`} alt={project.name} className="w-full h-full object-cover" />
                </div>
                <div className="p-6">
                  <div className="flex justify-between items-center mb-3">
                    <h3 className="text-xl font-bold text-gray-800">{project.name}</h3>
                    <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded">
                      {project.year}
                    </span>
                  </div>
                  <ul className="list-disc pl-5 space-y-2 text-gray-600 mb-4">
                    {project.details.map((detail, i) => (
                      <li key={i}>{detail}</li>
                    ))}
                  </ul>
                  <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors duration-300">
                    View Project
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
      
      {/* Skills Section */}
      <section id="skills" className="py-20 bg-gray-100">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">Skills & Certifications</h2>
          
          {/* Technical Skills */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Languages</h3>
              <div className="flex flex-wrap gap-2">
                {skills.languages.map((skill, index) => (
                  <span 
                    key={index} 
                    className="bg-blue-100 text-blue-800 text-sm font-medium px-3 py-1 rounded-full"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
            
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Technologies</h3>
              <div className="flex flex-wrap gap-2">
                {skills.technologies.map((tech, index) => (
                  <span 
                    key={index} 
                    className="bg-green-100 text-green-800 text-sm font-medium px-3 py-1 rounded-full"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>
            
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Additional</h3>
              <div className="flex flex-wrap gap-2">
                {skills.additional.map((skill, index) => (
                  <span 
                    key={index} 
                    className="bg-purple-100 text-purple-800 text-sm font-medium px-3 py-1 rounded-full"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          </div>
          
          {/* Certifications */}
          <h3 className="text-2xl font-bold text-gray-800 mb-6">Certifications</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {certifications.map((cert, index) => (
              <div key={index} className="bg-white rounded-lg shadow-md p-6 flex items-center">
                <div className="bg-gray-200 h-16 w-16 rounded-full flex items-center justify-center mr-4">
                  <svg className="w-8 h-8 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-lg font-medium text-gray-800">{cert.name}</h4>
                  <p className="text-gray-600">Issued {cert.year}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
      
      {/* Contact Section */}
      <section id="contact" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">Get In Touch</h2>
          <div className="flex flex-col md:flex-row">
            <div className="md:w-1/2 mb-8 md:mb-0">
              <div className="bg-white rounded-lg shadow-md p-6">
                <h3 className="text-xl font-bold text-gray-800 mb-4">Contact Information</h3>
                <div className="space-y-4">
                  <div className="flex items-start">
                    <div className="bg-blue-100 p-2 rounded-full mr-4">
                      <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                      </svg>
                    </div>
                    <div>
                      <p className="font-medium text-gray-800">Location</p>
                      <p className="text-gray-600">{personalInfo.location}</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <div className="bg-blue-100 p-2 rounded-full mr-4">
                      <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <div>
                      <p className="font-medium text-gray-800">Email</p>
                      <p className="text-gray-600">{personalInfo.email}</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <div className="bg-blue-100 p-2 rounded-full mr-4">
                      <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                      </svg>
                    </div>
                    <div>
                      <p className="font-medium text-gray-800">Phone</p>
                      <p className="text-gray-600">{personalInfo.phone}</p>
                    </div>
                  </div>
                  
                  <div className="flex space-x-4 mt-6">
                    <a href={`https://linkedin.com/in/${personalInfo.linkedin}`} target="_blank" rel="noopener noreferrer" className="bg-blue-600 text-white p-2 rounded-full hover:bg-blue-700 transition-colors duration-300">
                      <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                      </svg>
                    </a>
                    <a href={`https://github.com/${personalInfo.github}`} target="_blank" rel="noopener noreferrer" className="bg-gray-800 text-white p-2 rounded-full hover:bg-gray-900 transition-colors duration-300">
                      <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                      </svg>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="md:w-1/2 md:pl-8">
              <form className="bg-white rounded-lg shadow-md p-6">
                <div className="grid grid-cols-2 gap-4 mb-4">
                  <div>
                    <label htmlFor="first-name" className="block text-sm font-medium text-gray-700 mb-1">
                      First Name
                    </label>
                    <input
                      type="text"
                      id="first-name"
                      className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>
                  <div>
                    <label htmlFor="last-name" className="block text-sm font-medium text-gray-700 mb-1">
                      Last Name
                    </label>
                    <input
                      type="text"
                      id="last-name"
                      className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>
                </div>
                
                <div className="mb-4">
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                    Email
                  </label>
                  <input
                    type="email"
                    id="email"
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                
                <div className="mb-4">
                  <label htmlFor="subject" className="block text-sm font-medium text-gray-700 mb-1">
                    Subject
                  </label>
                  <input
                    type="text"
                    id="subject"
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                
                <div className="mb-6">
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-1">
                    Message
                  </label>
                  <textarea
                    id="message"
                    rows="4"
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  ></textarea>
                </div>
                
                <button
                  type="submit"
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors duration-300"
                >
                  Send Message
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>
      
      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="mb-4 md:mb-0">
              <h3 className="text-xl font-bold">{personalInfo.name}</h3>
              <p className="text-gray-400">Data Scientist | Entrepreneur | Tech Enthusiast</p>
            </div>
            
            <div className="flex space-x-4">
              <a href={`https://linkedin.com/in/${personalInfo.linkedin}`} target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors duration-300">
                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
              </a>
              <a href={`https://github.com/${personalInfo.github}`} target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors duration-300">
                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
              </a>
            </div>
          </div>
          
          <hr className="border-gray-700 my-6" />
          
          <div className="text-center text-gray-400 text-sm">
            <p>&copy; {new Date().getFullYear()} {personalInfo.name}. All rights reserved.</p>
            <p className="mt-2">Designed and developed with passion</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;