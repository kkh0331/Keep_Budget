import React from 'react';
import MoveRegionChange from '../common/MoveRegionChange';
import MoveHouseChange from '../common/MoveHouseChange';
import MoveHouseTypeChange from '../common/MoveHouseTypeChange';

const RightTop = (props) => {

  const userInfo = props.userInfo;
  const {getMoveRegion} = MoveRegionChange();
  const moveRegion = getMoveRegion(props.wantMoveRegion);
  const {getMoveHouse} = MoveHouseChange();
  const moveHouse = getMoveHouse(userInfo.moveHouse);
  const {getMoveHouseType} = MoveHouseTypeChange();
  const moveHouseType = getMoveHouseType(userInfo.moveHouseType)

  return (
    <div>
        <span style={{fontSize:"25px", color:"#ffb437", fontWeight:"bold"}}>{props.userInfo.userName}</span>님,
        <div style={{marginTop:"10px"}}>
            <span style={{fontWeight:"bold"}}>현재 상황 : </span>
            (연봉){userInfo.annualIncome}만원 (순자산){userInfo.totalAmount}만원 보유
        </div>
        <div style={{marginTop:"10px"}}>
            <span style={{fontWeight:"bold"}}>희망 사항 : </span>
            {userInfo.moveDate}개월 후, {moveRegion} {moveHouse} {moveHouseType} {userInfo.moveSize}평으로 이사
        </div>
    </div>
  );
};

export default RightTop;