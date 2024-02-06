import React from 'react'
import { Link } from 'react-router-dom';

export default function About() {
  return (
    <>
    <div>
    <header className="bg-dark text-white py-4">
      <div className="container">
        <h1>About Us</h1>
      </div>
    </header>

    <main className="py-3 ">

      <div className="container" >
        <h3 className="py-2">About the project</h3>
        <div className='px-3 ' style={{ paddingTop: 5}}>

          <p className="mb-2">This project is made for ios class</p>
          <p className="mb-2">It's made by Omair Hamd alla </p>
          <p className="mb-2">And it was using React and Bootstrap styling </p>

        </div>
      </div>
    </main>

    <div className="container">
      <h5 className="py-1">You can check more about our services here: </h5>
      <Link to="/services">
        <button className="btn btn-dark py-2">Go to Services</button>
      </Link>
    </div>

  

  </div>
      
    </>
  )
}
