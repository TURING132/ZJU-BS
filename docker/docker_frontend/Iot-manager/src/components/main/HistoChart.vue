<template>
    <div>
        <div class="title-wrapper">设备统计</div>
        <div class="chart-wrapper">
            <div class="d3HisChart">
            </div>
        </div>
    </div>
</template>

<script>
import * as d3 from 'd3';
export default {
    
    props:{
        devices: {
            type: Array,
            required: true,
            default: () => []
        },
        deviceType:{
            type: Array,
            required: true,
            default: () => []
        },
    },
    watch:{
        devices: function(newDevices, oldDevices) {
            this.drawHistogram();
        },
    },
    methods:{
        drawHistogram(){
            d3.select('.d3HisChart svg').remove();
            // 统计类型
            const typeCounts = this.devices.reduce((acc,device)=>{
                const type = device.type;
                acc[type] = (acc[type]||0) + 1;
                return acc;
            },{})


            // 产生渐变颜色
            const colorScale = d3.scaleLinear().domain([0, 1]).range(['#fff', '#144E2E']);

            // 生成渐变颜色数组
            const lenghthOfType = Object.keys(typeCounts).length;
            const gradientColors = Array.from({ length: lenghthOfType }, (_, index) => {
                const t = index / (lenghthOfType - 1); // 生成 0 到 1 之间的分数
                return colorScale(t);
            });

            // 随机打乱数组顺序
            const shuffledColors = d3.shuffle(gradientColors);
            const data = Object.keys(typeCounts).map((type, index) => ({
                type: this.deviceType.find(device => device.type === type).cn,
                count: typeCounts[type],
                color: shuffledColors[index % lenghthOfType] // 循环使用颜色数组
            }));
            
            
            //设置svg的尺寸
            const width = 350;
            const height = 200;
            const margin = {top:20,right:0,bottom:20,left:35}
            
            //创建svg容器
            const svg = d3.select('.d3HisChart')
                .append('svg')
                .attr('width', width + margin.left + margin.right)
                .attr('height', height + margin.top + margin.bottom)
                .append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // 设置比例尺
            const x = d3.scaleBand().range([0, width]).padding(0.3).domain(data.map(d => d.type));
            const y = d3.scaleLinear().range([height, 0]).domain([0, d3.max(data, d => d.count)]);


            // 绘制条形图
            svg.selectAll('.bar')
                .data(data)
                .enter().append('rect')
                .attr('class', 'bar')
                .attr('x', d => x(d.type))
                .attr('width', x.bandwidth())
                .attr('y', d => y(d.count))
                .attr('height', d => height - y(d.count))
                .attr('fill', d => d.color);

            // 绘制x轴
            svg.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(x))
                .style('color','#144E2E');

            // 绘制y轴
            svg.append('g')
                .call(d3.axisLeft(y))
                .style('color','#144E2E');
        }
    },
    mounted(){
        this.drawHistogram()
    }
}
</script>

<style scoped>
.chart-wrapper{
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
    letter-spacing: 0.1em;;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>