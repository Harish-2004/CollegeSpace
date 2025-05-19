import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import InterviewCard from './components/InterviewCard';
import './styles/Interview.css';
import { API_BASE_URL } from '../../config';

export default function Interview() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState('all');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchInterviews = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`${API_BASE_URL}/interview`);
        if (response.data && Array.isArray(response.data)) {
          setStudents(response.data);
        } else {
          setStudents([]);
        }
        setError(null);
      } catch (err) {
        setError('Failed to fetch interview experiences. Please try again later.');
        console.error('Error fetching interviews:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchInterviews();
  }, []);

  const handleAddInterview = () => {
    navigate("/Intform");
  };

  const filteredStudents = students.filter(student => {
    if (!student) return false;
    
    const matchesSearch = 
      (student.company?.toLowerCase().includes(searchTerm.toLowerCase()) || false) ||
      (student.role?.toLowerCase().includes(searchTerm.toLowerCase()) || false) ||
      (student.name?.toLowerCase().includes(searchTerm.toLowerCase()) || false);
    
    const matchesFilter = 
      filter === 'all' || 
      (filter === 'success' && student.status?.toLowerCase() === 'selected') ||
      (filter === 'pending' && student.status?.toLowerCase() === 'pending') ||
      (filter === 'rejected' && student.status?.toLowerCase() === 'rejected');

    return matchesSearch && matchesFilter;
  });

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="interview-container">
      <div className="interview-header">
        <h2>Interview Experiences</h2>
        <div className="controls">
          <div className="search-box">
            <input
              type="text"
              placeholder="Search by company, role, or name..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
          <div className="filter-box">
            <select value={filter} onChange={(e) => setFilter(e.target.value)}>
              <option value="all">All Status</option>
              <option value="success">Selected</option>
              <option value="pending">Pending</option>
              <option value="rejected">Rejected</option>
            </select>
          </div>
          <button className="add-button" onClick={handleAddInterview}>
            Add Interview Experience
          </button>
        </div>
      </div>

      {filteredStudents.length === 0 ? (
        <div className="no-results">
          No interview experiences found matching your criteria.
        </div>
      ) : (
        <div className="interview-list">
          {filteredStudents.map((student, index) => (
            <InterviewCard key={student._id || index} student={student} />
          ))}
        </div>
      )}
    </div>
  );
} 