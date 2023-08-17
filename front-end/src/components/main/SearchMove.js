import React, { useState } from 'react'
import RegionCategory from '../userinput/RegionCategory';
import './main.css'

const SearchMove = ({setWantMoveRegion}) => {

  const [region, setRegion] = useState(0)

  const handleChangedMoveRegionChange = (e) => {
      setRegion(e.target.value);
  }

  const handleChangedMoveRegionClick = () => {
      setWantMoveRegion(region)
  }

  return (
    <div style={{display:'flex', justifyContent:'center', alignItems:'center'}}>
        <RegionCategory handleCurrentRegionChange={handleChangedMoveRegionChange}></RegionCategory>
        <button className='btnType02' onClick={handleChangedMoveRegionClick}>지역변경</button>
    </div>
  );
};

export default SearchMove;