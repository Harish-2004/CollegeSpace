import React from 'react';

export default function InterviewCard (props) {
  
  return (
    <div className="student-card">
      <h2>{props.student.name}</h2>
      <p>Roll Number: {props.student.email}</p>
    </div>
  );
};
