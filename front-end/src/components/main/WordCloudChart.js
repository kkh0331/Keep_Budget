import React, { useEffect } from 'react';
import WordCloud from 'react-d3-cloud';

const WordCloudChart = ({wordCloudData}) => {

    return (
        <div style={{textAlign:"center", margin:"auto", width:"350px", height:"350px"}}>
            <WordCloud 
                data={wordCloudData}
                fontSize={(word) => Math.log2(word.value) * 30}
                font="Times"
            />
        </div>
    );
};

export default WordCloudChart;