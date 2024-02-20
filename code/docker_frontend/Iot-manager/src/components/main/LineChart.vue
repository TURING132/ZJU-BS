<template>
    <div>
        <div class="title-wrapper">流量统计</div>
        <div class="line-wrapper">
            <div class="d3LineChart">
            </div>
        </div>
    </div>
  
</template>

<script>
import * as d3 from 'd3';
export default {
    data(){
        return{
            trafficData: Array.from({ length: 10 }, () => 0),
            intervalId: null,
        }

    },
    mounted(){
        // 每2秒请求一次当前流量
        this.intervalId = setInterval(()=>{
            this.fetchTrafficData();
            this.updateChart();
        },4000);

        this.setupChart();
    },
    beforeDestroy() {
        clearInterval(this.intervalId);
    },
    methods:{
        async fetchTrafficData(){
            let newData
            try{
                    const response = await fetch(`http://127.0.0.1:8000/mqtt/bytes`,{
                        method: 'GET',
                    });
                    if (response.ok) {
                        const jsonResponse = await response.json();
                        newData = jsonResponse.sent_bytes/1000
                    } else {
                        alert(`网络错误: ${response.message}`);
                    }
                } catch (error) {
                    console.log(error)
                    alert(`网络错误`);
                }
            // 保持 trafficData 长度为 10
            this.trafficData.shift(); // 去掉第一个数据
            this.trafficData.push(newData); // 将新数据添加到末尾; // for test
        },
        setupChart(){
            //设置svg的尺寸
            const width = 350;
            const height = 200;
            const margin = {top:20,right:20,bottom:20,left:30};
            //创建svg容器
            const svg = d3.select('.d3LineChart')
                .append('svg')
                .attr('width', width + margin.left + margin.right)
                .attr('height', height + margin.top + margin.bottom)
                .append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            // 添加横纵轴
            svg.append('g').attr('class', 'x-axis').attr('transform', `translate(0,${height})`).style('color','#144E2E');;
            svg.append('g').attr('class', 'y-axis').style('color','#144E2E');;
            svg.append('text')
            .attr('y', -15)
            .attr('x', 0)
            .attr('dy', '1em')
            .style('font-size', '12px')
            .style('fill','#144E2E')
            .text('单位 (KB)');
            
            
            // 定义线段函数
            const line = d3
                .line()
                .x((d, i) => xScale(i))
                .y(d => yScale(d));

            // 将折线添加到图表中
            svg.append('path')
            .attr('class', 'line')
            .attr('fill', 'none')
            .attr('stroke', '#144E2E');

            this.updateChart(); // 初始化图表
        },
        updateChart() {
            const svg = d3.select('.d3LineChart').select('svg').select('g');

            // 更新 x 轴和 y 轴的比例尺的域（domain）
            const xScale = d3.scaleLinear().domain([0, this.trafficData.length - 1]).range([0, 350]);
            const yScale = d3.scaleLinear().domain([0, d3.max(this.trafficData)]).range([200, 0]);

            // 选择 x 轴和 y 轴，并更新它们的比例尺
            svg.select('.x-axis').call(d3.axisBottom(xScale));
            svg.select('.y-axis').call(d3.axisLeft(yScale));

            // 更新折线的路径
            svg.select('.line').datum(this.trafficData).attr('d', d3.line().x((d, i) => xScale(i)).y(d => yScale(d)));
        },
        
    }

}
</script>

<style scoped>
.line-wrapper{
    width: 400px;
    height: 250px;
    box-sizing: border-box;
    background-color: rgb(255, 255, 255,0.4);
    border-radius: 10px;
}
.title-wrapper{
    height: 30px;
    color: #fff;
    font-weight:bold;
    letter-spacing: 0.1em;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>