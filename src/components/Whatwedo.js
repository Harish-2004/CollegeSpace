import React, { useState } from 'react';
import './Whatwedo.css';
import { FaGraduationCap, FaUserTie, FaCalendarAlt, FaBell, FaUserCircle } from 'react-icons/fa';

const Whatwedo = () => {
  const [activeTab, setActiveTab] = useState('placements');

  const menuItems = [
    { id: 'placements', icon: <FaUserTie />, label: 'Placements' },
    { id: 'interviews', icon: <FaGraduationCap />, label: 'Interview Experiences' },
    { id: 'alerts', icon: <FaBell />, label: 'Job and Internship Alerts' },
    { id: 'events', icon: <FaCalendarAlt />, label: 'Upcoming Events' },
    { id: 'profile', icon: <FaUserCircle />, label: 'Student Profile' }
  ];

  const content = {
    placements: {
      title: "Placement Opportunities",
      description: "Access comprehensive placement information, company details, and recruitment processes. Stay updated with the latest job openings and placement statistics."
    },
    interviews: {
      title: "Interview Experiences",
      description: "Learn from real interview experiences shared by seniors. Get insights into company interview processes, frequently asked questions, and preparation tips."
    },
    alerts: {
      title: "Job & Internship Alerts",
      description: "Never miss an opportunity! Get instant notifications about new job postings, internship openings, and application deadlines."
    },
    events: {
      title: "Upcoming Events",
      description: "Stay informed about campus recruitment drives, workshops, seminars, and career fairs. Mark your calendar and prepare in advance."
    },
    profile: {
      title: "Student Profile",
      description: "Create and manage your professional profile. Showcase your skills, projects, and achievements to potential employers."
    }
  };

  const handleTabClick = (tabId) => {
    setActiveTab(tabId);
  };

  return (
    <div className='container'>
      <div className='left-panel'>
        <h2 className='panel-title'>Quick Access</h2>
        <ul className='menu-list'>
          {menuItems.map((item) => (
            <li 
              key={item.id}
              className={`menu-item ${activeTab === item.id ? 'active' : ''}`}
              onClick={() => handleTabClick(item.id)}
            >
              <span className='icon'>{item.icon}</span>
              <span className='label'>{item.label}</span>
            </li>
          ))}
        </ul>
      </div>
      <div className='right-panel'>
        <div className='content-box'>
          <h2 className='content-title'>{content[activeTab].title}</h2>
          <p className='content-description'>{content[activeTab].description}</p>
          <button className='action-button'>Learn More</button>
        </div>
      </div>
    </div>
  );
};

export default Whatwedo; 