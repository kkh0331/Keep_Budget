import {useState} from 'react';

const MoveHouseChange = () => {

    const houseMap = {
        "apart" : "아파트",
        "officetel" : "오피스텔",
        default : "error",
    }

    const getMoveHouse = (moveHouse) => {
        return houseMap[moveHouse] || houseMap.default;
    }

    return {getMoveHouse};
};

export default MoveHouseChange;