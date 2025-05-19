import React, { useState } from 'react';
import './InterviewPrep.css';

const InterviewPrep = () => {
  const [expandedCompany, setExpandedCompany] = useState(null);

  const toggleCompany = (company) => {
    setExpandedCompany(expandedCompany === company ? null : company);
  };

  const companies = [
    {
      name: 'Bloomberg',
      logo: '📈',
      topics: [
        'Data Structures and Algorithms',
        'System Design',
        'C++ Programming',
        'Database Concepts',
        'Object-Oriented Design',
        'Concurrency and Multithreading'
      ],
      resources: [
        {
          title: 'Bloomberg LeetCode Questions',
          url: 'https://leetcode.com/company/bloomberg/'
        },
        {
          title: 'GeeksforGeeks Preparation Guide',
          url: 'https://www.geeksforgeeks.org/bloomberg-interview-preparation/'
        },
        {
          title: 'Bloomberg Interview Experience',
          url: 'https://www.geeksforgeeks.org/bloomberg-interview-experience/'
        }
      ]
    },
    {
      name: 'Microsoft',
      logo: '💻',
      topics: [
        'Problem Solving',
        'Data Structures',
        'System Design',
        'Coding Questions',
        'Design Patterns',
        'API Design'
      ],
      resources: [
        {
          title: 'Microsoft LeetCode Questions',
          url: 'https://leetcode.com/company/microsoft/'
        },
        {
          title: 'GeeksforGeeks Preparation Guide',
          url: 'https://www.geeksforgeeks.org/microsoft-interview-preparation/'
        },
        {
          title: 'Microsoft Interview Experience',
          url: 'https://www.geeksforgeeks.org/microsoft-interview-experience/'
        }
      ]
    },
    {
      name: 'Google',
      logo: '🔍',
      topics: [
        'Algorithms',
        'Data Structures',
        'System Design',
        'Coding Questions',
        'Machine Learning Basics',
        'Big Data Concepts'
      ],
      resources: [
        {
          title: 'Google LeetCode Questions',
          url: 'https://leetcode.com/company/google/'
        },
        {
          title: 'GeeksforGeeks Preparation Guide',
          url: 'https://www.geeksforgeeks.org/google-interview-preparation/'
        },
        {
          title: 'Google Interview Experience',
          url: 'https://www.geeksforgeeks.org/google-interview-experience/'
        }
      ]
    }
  ];

  return (
    <div className="interview-prep-container">
      <h2>Interview Preparation</h2>
      <div className="company-sections">
        {companies.map((company) => (
          <div 
            key={company.name}
            className={`company-box ${expandedCompany === company.name ? 'expanded' : ''}`}
            onClick={() => toggleCompany(company.name)}
          >
            <h3>
              <span className="company-logo">{company.logo}</span>
              {company.name}
            </h3>
            <div className="prep-content">
              <h4>Technical Interview Topics</h4>
              <ul>
                {company.topics.map((topic, index) => (
                  <li key={index}>{topic}</li>
                ))}
              </ul>
              <div className="resources">
                <h5>Recommended Resources</h5>
                {company.resources.map((resource, index) => (
                  <a 
                    key={index}
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    onClick={(e) => e.stopPropagation()}
                  >
                    {resource.title}
                  </a>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default InterviewPrep; 