import React, { useState, useEffect } from 'react';
import './StudentProfile.css';
import axios from 'axios';

const StudentProfile = () => {
  const [studentData, setStudentData] = useState({
    name: '',
    email: '',
    contactno: '',
    startYear: '',
    branch: '',
    academicScores: {
      semester1: '',
      semester2: '',
      semester3: '',
      semester4: '',
      semester5: '',
      semester6: '',
      semester7: '',
      semester8: ''
    },
    certifications: {
      tenth: {
        board: '',
        year: '',
        percentage: '',
        school: ''
      },
      twelfth: {
        board: '',
        year: '',
        percentage: '',
        school: ''
      }
    },
    projects: [],
    github: '',
    skills: [],
    internships: [],
    fullTimeJobs: []
  });

  const [dispensaryRequest, setDispensaryRequest] = useState({
    reason: '',
    date: '',
    status: 'pending'
  });

  const [showDispensaryForm, setShowDispensaryForm] = useState(false);
  const [requestSubmitted, setRequestSubmitted] = useState(false);

  useEffect(() => {
    // Fetch student data from backend
    const fetchStudentData = async () => {
      try {
        const response = await axios.get('http://localhost:5001/studentProfile');
        setStudentData(response.data);
      } catch (error) {
        console.error('Error fetching student data:', error);
      }
    };

    fetchStudentData();
  }, []);

  const handleDispensarySubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5001/dispensaryRequest', {
        ...dispensaryRequest,
        studentId: studentData._id,
        studentName: studentData.name
      });
      
      if (response.data.success) {
        setRequestSubmitted(true);
        setShowDispensaryForm(false);
        setDispensaryRequest({
          reason: '',
          date: '',
          status: 'pending'
        });
      }
    } catch (error) {
      console.error('Error submitting dispensary request:', error);
    }
  };

  const handleDispensaryChange = (e) => {
    const { name, value } = e.target;
    setDispensaryRequest(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="student-profile-container">
      <h2>Student Profile</h2>
      
      <div className="profile-section">
        <h3>Personal Information</h3>
        <div className="info-grid">
          <div className="info-item">
            <span className="label">Name:</span>
            <span className="value">{studentData.name}</span>
          </div>
          <div className="info-item">
            <span className="label">Email:</span>
            <span className="value">{studentData.email}</span>
          </div>
          <div className="info-item">
            <span className="label">Contact Number:</span>
            <span className="value">{studentData.contactno}</span>
          </div>
          <div className="info-item">
            <span className="label">Start Year:</span>
            <span className="value">{studentData.startYear}</span>
          </div>
          <div className="info-item">
            <span className="label">Branch:</span>
            <span className="value">{studentData.branch}</span>
          </div>
        </div>
      </div>

      <div className="profile-section">
        <h3>Academic Performance</h3>
        <div className="academic-grid">
          {Object.entries(studentData.academicScores).map(([semester, score]) => (
            <div key={semester} className="academic-item">
              <span className="label">{semester.replace('semester', 'Semester ')}:</span>
              <span className="value">{score || 'Not Available'}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="profile-section">
        <h3>School Certifications</h3>
        <div className="certification-grid">
          <div className="certification-item">
            <h4>10th Standard</h4>
            <div className="cert-details">
              <div className="detail-item">
                <span className="label">Board:</span>
                <span className="value">{studentData.certifications.tenth.board || 'Not Available'}</span>
              </div>
              <div className="detail-item">
                <span className="label">Year:</span>
                <span className="value">{studentData.certifications.tenth.year || 'Not Available'}</span>
              </div>
              <div className="detail-item">
                <span className="label">Percentage:</span>
                <span className="value">{studentData.certifications.tenth.percentage || 'Not Available'}</span>
              </div>
              <div className="detail-item">
                <span className="label">School:</span>
                <span className="value">{studentData.certifications.tenth.school || 'Not Available'}</span>
              </div>
            </div>
          </div>

          <div className="certification-item">
            <h4>12th Standard</h4>
            <div className="cert-details">
              <div className="detail-item">
                <span className="label">Board:</span>
                <span className="value">{studentData.certifications.twelfth.board || 'Not Available'}</span>
              </div>
              <div className="detail-item">
                <span className="label">Year:</span>
                <span className="value">{studentData.certifications.twelfth.year || 'Not Available'}</span>
              </div>
              <div className="detail-item">
                <span className="label">Percentage:</span>
                <span className="value">{studentData.certifications.twelfth.percentage || 'Not Available'}</span>
              </div>
              <div className="detail-item">
                <span className="label">School:</span>
                <span className="value">{studentData.certifications.twelfth.school || 'Not Available'}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="profile-section">
        <h3>Projects</h3>
        <div className="projects-grid">
          {studentData.projects && studentData.projects.length > 0 ? (
            studentData.projects.map((project, index) => (
              <div key={index} className="project-item">
                <h4>{project.title}</h4>
                <p className="project-description">{project.description}</p>
                {project.technologies && (
                  <div className="technologies">
                    {project.technologies.map((tech, techIndex) => (
                      <span key={techIndex} className="tech-tag">{tech}</span>
                    ))}
                  </div>
                )}
                {project.githubLink && (
                  <a href={project.githubLink} target="_blank" rel="noopener noreferrer" className="github-link">
                    View on GitHub
                  </a>
                )}
              </div>
            ))
          ) : (
            <p>No projects available</p>
          )}
        </div>
      </div>

      <div className="profile-section">
        <h3>GitHub Profile</h3>
        <div className="github-section">
          {studentData.github ? (
            <a href={studentData.github} target="_blank" rel="noopener noreferrer" className="github-profile-link">
              View GitHub Profile
            </a>
          ) : (
            <p>GitHub profile not available</p>
          )}
        </div>
      </div>

      <div className="profile-section">
        <h3>Skills</h3>
        <div className="skills-container">
          {studentData.skills && studentData.skills.length > 0 ? (
            studentData.skills.map((skill, index) => (
              <span key={index} className="skill-tag">{skill}</span>
            ))
          ) : (
            <p>No skills listed</p>
          )}
        </div>
      </div>

      <div className="profile-section">
        <h3>Internships</h3>
        <div className="internships-grid">
          {studentData.internships && studentData.internships.length > 0 ? (
            studentData.internships.map((internship, index) => (
              <div key={index} className="internship-item">
                <h4>{internship.company}</h4>
                <p className="internship-role">Role: {internship.role}</p>
                <p className="internship-duration">Duration: {internship.duration}</p>
                <p className="internship-description">{internship.description}</p>
              </div>
            ))
          ) : (
            <p>No internships available</p>
          )}
        </div>
      </div>

      <div className="profile-section">
        <h3>Full-Time Offers</h3>
        <div className="fulltime-grid">
          {studentData.fullTimeJobs && studentData.fullTimeJobs.length > 0 ? (
            studentData.fullTimeJobs.map((job, index) => (
              <div key={index} className="fulltime-item">
                <h4>{job.company}</h4>
                <p className="fulltime-role">Role: {job.role}</p>
                <p className="fulltime-duration">Duration: {job.duration}</p>
                <p className="fulltime-description">{job.description}</p>
              </div>
            ))
          ) : (
            <p>No full-time offers available</p>
          )}
        </div>
      </div>

      <div className="profile-section">
        <h3>Dispensary Services</h3>
        <div className="dispensary-section">
          {!showDispensaryForm && !requestSubmitted && (
            <button 
              className="request-button"
              onClick={() => setShowDispensaryForm(true)}
            >
              Request Dispensary Service
            </button>
          )}

          {showDispensaryForm && (
            <form className="dispensary-form" onSubmit={handleDispensarySubmit}>
              <div className="form-group">
                <label htmlFor="reason">Reason for Visit:</label>
                <textarea
                  id="reason"
                  name="reason"
                  value={dispensaryRequest.reason}
                  onChange={handleDispensaryChange}
                  required
                  placeholder="Please describe your symptoms or reason for visit"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="date">Preferred Date:</label>
                <input
                  type="date"
                  id="date"
                  name="date"
                  value={dispensaryRequest.date}
                  onChange={handleDispensaryChange}
                  required
                />
              </div>

              <div className="form-actions">
                <button type="submit" className="submit-button">Submit Request</button>
                <button 
                  type="button" 
                  className="cancel-button"
                  onClick={() => setShowDispensaryForm(false)}
                >
                  Cancel
                </button>
              </div>
            </form>
          )}

          {requestSubmitted && (
            <div className="request-success">
              <p>Your dispensary request has been submitted successfully!</p>
              <button 
                className="new-request-button"
                onClick={() => {
                  setRequestSubmitted(false);
                  setShowDispensaryForm(true);
                }}
              >
                Submit New Request
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default StudentProfile;