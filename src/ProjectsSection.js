import React from 'react';

const ProjectsSection = () => {
  // Updated projects data with custom image paths
  const projects = [
    {
      name: "NEO NET ENTERPRISE",
      year: "2025",
      image: "/assets/image/neo_net_enterprise.jpg", // Path to your custom image
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
      image: "/assets/image/paper_trading_platform.jpg", // Path to your custom image
      details: [
        "Architected full-stack trading simulation using C++, REST APIs, and SQL databases",
        "Integrated real-time market data processing with 99.7% uptime reliability"
      ],
      github: "https://github.com/prathamparakh"
    },
    {
      name: "AIRLINE NETWORK ANALYSIS",
      year: "2024",
      image: "/assets/image/airline_network_analysis.jpg", // Path to your custom image
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
      image: "/assets/image/cvp_analysis.jpg", // Path to your custom image
      details: [
        "Developed a Cost-Volume-Profit Analysis tool for financial decision-making",
        "Created interactive visualizations of break-even analysis and profitability scenarios",
        "Implemented sensitivity analysis features for business scenario planning"
      ],
      github: "https://github.com/prathamparakh/CVP-Analysis"
    }
  ];

  return (
    <section id="projects" className="py-20 bg-white">
      <div className="container mx-auto px-6">
        <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">Technical Projects</h2>
        
        {/* Improved grid with better spacing and alignment */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
          {projects.map((project, index) => (
            <div key={index} className="bg-white rounded-lg shadow-xl overflow-hidden hover:shadow-2xl transition-shadow duration-300">
              <div className="bg-gray-200 h-52 relative overflow-hidden">
                {/* Using custom images with fallback */}
                <img 
                  src={project.image}
                  alt={project.name} 
                  className="w-full h-full object-cover transition-transform duration-300 hover:scale-105" 
                  onError={(e) => {
                    // Fallback to placeholder if image fails to load
                    e.target.src = `https://via.placeholder.com/600x300?text=${encodeURIComponent(project.name)}`;
                  }}
                />
              </div>
              
              <div className="p-6">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-xl font-bold text-gray-800">{project.name}</h3>
                  <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-3 py-1 rounded-full">
                    {project.year}
                  </span>
                </div>
                
                {/* Improved list styling with better spacing */}
                <ul className="list-disc pl-5 space-y-2 text-gray-600 mb-6 min-h-[120px]">
                  {project.details.map((detail, i) => (
                    <li key={i} className="text-sm md:text-base">{detail}</li>
                  ))}
                </ul>
                
                {/* Enhanced button styling */}
                <a 
                  href={project.github} 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 px-4 rounded-md transition-colors duration-300 inline-block text-center"
                  onClick={(e) => {
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