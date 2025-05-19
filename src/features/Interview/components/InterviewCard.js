import React from 'react';
import '../styles/InterviewCard.css';

export default function InterviewCard({ student }) {
  return (
    <div className="interview-card">
      <div className="card-header">
        <div className="company-info">
          <h3 className="company-name">{student.company}</h3>
          <span className="interview-date">{new Date(student.date).toLocaleDateString()}</span>
        </div>
        <div className="role-info">
          <span className="role">{student.role}</span>
          <span className="status">{student.status}</span>
        </div>
      </div>
      
      <div className="card-content">
        <div className="experience-section">
          <h4>Interview Experience</h4>
          <p className="experience-text">{student.experience}</p>
        </div>
        
        <div className="details-section">
          <div className="detail-item">
            <span className="detail-label">Round:</span>
            <span className="detail-value">{student.round}</span>
          </div>
          <div className="detail-item">
            <span className="detail-label">Duration:</span>
            <span className="detail-value">{student.duration}</span>
          </div>
          <div className="detail-item">
            <span className="detail-label">Difficulty:</span>
            <span className={`difficulty-badge ${student.difficulty?.toLowerCase() || 'medium'}`}>
              {student.difficulty || 'Medium'}
            </span>
          </div>
        </div>
      </div>

      <div className="card-footer">
        <div className="student-info">
          <span className="student-name">{student.name}</span>
          <span className="student-email">{student.email}</span>
        </div>
        <div className="tags">
          {student.tags?.map((tag, index) => (
            <span key={index} className="tag">{tag}</span>
          ))}
        </div>
      </div>
    </div>
  );
} 