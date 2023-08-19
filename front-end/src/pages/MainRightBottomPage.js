import axios from 'axios';
import React, { useEffect, useState } from 'react'
import RecommendElement from '../components/main/RecommendElement';

const MainRightBottomPage = ({userInfo, wantMoveRegion}) => {

    const [recommendList, setRecommendList] = useState([]);

    useEffect(()=>{
        getRecommendList();
    },[wantMoveRegion])

    const getRecommendList = () => {
        let option = {
            url: "/recommend",
            method: "POST",
            data:{
                user_info: userInfo,
                want_move_region : wantMoveRegion
            }
        }
        axios(option).then(({data}) => {
            console.log("recommend : ", data);
            setRecommendList(data)
        }).catch((error) => {
            console.log(error);
        })
    }

    return (
        <div>
            {recommendList.map((item) => {
                return <RecommendElement item={item}></RecommendElement>
            })}
        </div>
    );
};

export default MainRightBottomPage;