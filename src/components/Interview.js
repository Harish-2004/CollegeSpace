import React , { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import InterviewCard from './InterviewCard';

export default function Interview()
{const [students, setStudents] = useState([]);
    const navigate=useNavigate();
    const handle=()=>{navigate("/IntForm")}
    useEffect(()=>
    {axios.get('http://localhost:5001/interview')
      .then(response => {
       const responseData = response.data;
       setStudents(responseData)
        console.log(responseData)
      })
      .catch(error => {
        console.error(error);
      });
    })
    return <div>
        <h3>Interview Experiences</h3>
        {students.map(student => (
        <InterviewCard key={student._id} student={student} />
      ))}
      <button onClick={handle}>Add Interview Experience</button>
    </div>
}