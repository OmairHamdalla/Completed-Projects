import React from 'react'

export default function Contact() {
  return (
    <><div>
    <header className="bg-dark text-white py-4">
      <div className="container">
        <h1>Contact Us</h1>
      </div>
    </header>

    <main className="py-3">
      <div className="container">
        <p className="mb-1">Well I wish that this form works but its just visuals...</p>
        <p>But you can try and contact us through here anyway!</p>

        <form>

          <div className="mb-3">
            <label className="form-label">Name</label>
            <input type="text" className="form-control" placeholder="Enter your name" />
          </div>

          <div className="mb-3">
            <label className="form-label">Email address</label>
            <input type="email" className="form-control" id="email" placeholder="Enter your email"  />
          </div>

          <div className="mb-3">
            <label className="form-label">Message</label>
            <textarea className="form-control" rows="5" placeholder="Enter your message"></textarea>
          </div>

          <button className="btn btn-dark">Submit</button>

        </form>
      </div>
    </main>

  </div>

    </>
  )
}
