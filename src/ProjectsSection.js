import React from 'react';

const ProjectsSection = () => {
  // Updated projects data with working images and links
  const projects = [
    {
      name: "NEO NET ENTERPRISE",
      year: "2025",
      details: [
        "Engineered AI-powered business toolset using Python, TensorFlow, and AWS cloud services",
        "Implemented market prediction algorithms with 89% accuracy for financial forecasting",
        "Created automated workflows reducing administrative overhead by 65% for startups"
      ],
      github: "https://github.com/prathamparakh"
    },
    {
      name: "PAPER TRADING PLATFORM",
      year: "2023",
      details: [
        "Architected full-stack trading simulation using C++, REST APIs, and SQL databases",
        "Integrated real-time market data processing with 99.7% uptime reliability"
      ],
      github: "https://github.com/prathamparakh"
    },
    {
      name: "AIRLINE NETWORK ANALYSIS",
      year: "2024",
      details: [
        "Implemented Ford-Fulkerson algorithm to analyze and optimize airline network flow",
        "Visualized optimal paths and bottlenecks in airline transportation networks",
        "Applied graph theory concepts to solve real-world airline capacity problems"
      ],
      github: "https://github.com/prathamparakh/Airline_Network_Analysis_FordFulkerson"
    },
    {
      name: "CVP ANALYSIS",
      year: "2023",
      details: [
        "Developed a Cost-Volume-Profit Analysis tool for financial decision-making",
        "Created interactive visualizations of break-even analysis and profitability scenarios",
        "Implemented sensitivity analysis features for business scenario planning"
      ],
      github: "https://github.com/prathamparakh/CVP-Analysis"
    }
  ];

  return (
    <section id="projects" className="py-20">
      <div className="container mx-auto px-6">
        <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">Technical Projects</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {projects.map((project, index) => (
            <div key={index} className="bg-white rounded-lg shadow-lg overflow-hidden">
              <div className="bg-gray-300 h-48">
                {/* Using API placeholder images that work in this environment */}
                <img 
                  src={`/api/placeholder/600/300`} 
                  alt={project.name} 
                  className="w-full h-full object-cover" 
                />
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
                <a 
                  href={project.github} 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors duration-300 inline-block text-center"
                  onClick={(e) => {
                    // This ensures the link works properly by explicitly
                    // opening the URL in a new tab/window
                    e.preventDefault();
                    window.open(project.github, '_blank', 'noopener,noreferrer');
                  }}
                >
                  View Project
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ProjectsSection;