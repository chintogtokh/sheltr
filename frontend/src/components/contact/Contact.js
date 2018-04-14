import React, { Component } from 'react';
import './Contact.css';

class Contact extends Component {

    render() {
        return (
        <div>
            <main role="main">
                <div className="container">

                    <h1>Contact Us</h1>

                    <div>Hi there, we're four students at Monash Uni. We are (ordered alphabetically):</div>

                    <ul>
                    <li><b>Chintogtokh Batbold</b> - Enrolled in the Master of Information Technology program, with a Bachelor of Software Engineering & Computer Networking from the National University of Mongolia. Main strengths include full-stack development & network security. Currently working as a full-stack developer at Property Shell, previously worked as Software Engineering intern at Rolls-Royce plc.
                        </li>
                       <li><b>James Furnell</b> - Enrolled in the Master of Information Technology program, with a Bachelor of Accounting from Monash University. Main strengths are data analysis, forecasting, and visualization. Currently working as a part-time tutor at RMIT and previously worked as data analytics intern at Spotless Group Holdings.
                       </li>
                       <li><b>Sharmeen Kaur</b> - Enrolled in the Master of Business Information Systems program, with a Bachelor of Computer Engineer from Punjab Technical University. Main strengths are UI/UX design and Business Intelligence. Currently working as an attendant at Delaware North, previously worked as a Software Engineer at Capgemini.
                       </li>
                       <li><b>Wanping Yang</b> - Enrolled in the Master of Business Information Systems program, Bachelor of E-Commerce from Beijing Information & Technology University. Main strengths include e-commerce and project management. Previously worked as an intern at YongYou Software Co. Ltd.
                       </li>
                    </ul>
                </div>
            </main>
        </div>
        );
    }
}

export default Contact;
