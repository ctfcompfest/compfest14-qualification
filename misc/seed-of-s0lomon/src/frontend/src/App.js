import { BrowserRouter, Routes, Route} from "react-router-dom";
import Login from "./Login";
import Throne from "./Throne";


function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Login/>}/>
      <Route path="/throne" element={<Throne/>}/>
    </Routes>
    </BrowserRouter>
  );
}

export default App;
