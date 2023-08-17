import axios from 'axios';
import React, { useEffect, useState } from 'react';
import DonutChart from 'react-donut-chart';
import styled from "styled-components";

const ChartContainer = styled.div`
  width: 350px;
  height: 350px;
  margin: auto;
`;

const NewsDonutChart = ({moveRegion, handleStateClick}) => {

    const [negative, setNegative] = useState(0);
    const [neutrality, setNeutrality] = useState(0);
    const [positive, setPositive] = useState(0);

    useEffect(()=>{
        if(moveRegion){
            getRealStateRatio();
        }
    }, [moveRegion])

    const getRealStateRatio = () => {
        let option = {
            url: "/real_state_news_chart",
            method: "POST",
            data:{
                move_region: moveRegion,
            }
        }
        axios(option).then(({data}) => {
            console.log(data);
            setNegative(data.negative);
            setNeutrality(data.neutrality);
            setPositive(data.positive);
        }).catch((error) => {
            console.log(error);
        })
    }

    const data = [
        {
            label: '중립',
            value: neutrality,
        },
        {
            label: '긍정',
            value: positive,
        },
        {
            label: '부정',
            value: negative,
        },
    ]

    return (
        <ChartContainer>
            <DonutChart data={data} legend={false} width={350} height={350}
            colors={['#ffce0b','#0000ff','#990e17']} innerRadius={0.6} onClick={handleStateClick}></DonutChart>
        </ChartContainer>
    );
};

export default NewsDonutChart;