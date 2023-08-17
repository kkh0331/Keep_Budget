import {useState} from 'react';

const MoveHouseTypeChange = () => {

    const houseTypeMap = {
        "jeonse" : "전세",
        "purchaseSale" : "매매",
        "monthlyRent" : "월세",
        default: "error"
    };

    const getMoveHouseType = (moveHouseType) => {
        return houseTypeMap[moveHouseType] || houseTypeMap.default;
    };

    return {getMoveHouseType};
};

export default MoveHouseTypeChange;