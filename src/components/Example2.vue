<template>
  <div>
    <h1>例子2</h1>
    <h4>点击运行会运行example目录下的example.py</h4>
    <el-input v-model="mytext" placeholder="请输入内容"></el-input>
    <el-button plain @click="execExample">运行</el-button>
    <p v-if="cmdResult">{{ cmdResult }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cmdResult: "",
      cmdInput: "",
      mytext: ""
    };
  },
  methods: {
    execExample: function() {
      this.$execCmd(
        // 命令行怎么运行它就怎么写
        `python3 ./example/pywhatweb/example.py ` + this.mytext,
        // 加载动效的文字
        "运行python example :)",
        // 结果存放，如果按默认设定，在执行完成后：
        // `this['cmdResult'] = result`
        "cmdResult"
      );
    }
  }
};
</script>
