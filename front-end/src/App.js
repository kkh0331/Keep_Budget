import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import UserInputPage from './pages/UserInputPage';
import MainPage from './pages/MainPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/userinput' element={<UserInputPage/>}></Route>
        <Route path='/result' element={<MainPage/>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
