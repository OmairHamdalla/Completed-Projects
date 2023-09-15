import {Route, Routes, BrowserRouter} from 'react-router-dom'
import Home from "./components/Home";
import About from "./components/About";
import Contact from "./components/Contact";
import Services from "./components/Services";
import Layout from "./components/Layout";

function App() {
  return (
  <>
  <BrowserRouter>
  <Layout />
  <Routes>
    <Route path="/" element= {<Home />}/>
    <Route path="home" element= {<Home />}/>
    <Route path="contact" element= {<Contact />}/>
    <Route path="about" element= {<About />}/>
    <Route path="services" element= {<Services />}/>
  </Routes>
  </BrowserRouter>
  </>
  );
}

export default App;
