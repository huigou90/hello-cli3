<template>
  <div>
    <h1>例子1</h1>
    <h4>点击运行会运行example目录下的example.py</h4>
    <el-button plain @click="execExample">运行</el-button>
    <p v-if="cmdResult">{{ cmdResult }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cmdResult: "",
      cmdInput: ""
    };
  },
  methods: {
    execExample: function() {
      var thrift = require("thrift");
      var userService = require("@/api/userService.js");
      // eslint-disable-line no-unused-vars
      // var ttypes = require("@/api/test_types.js");
      var thriftConnection = thrift.createConnection("127.0.0.1", 8000);
      var thriftClient = thrift.createClient(userService, thriftConnection);
      thriftConnection.on("error", function(e) {
        console.log(e);
      });
      console.log("success");
      var dic = { name: "jack" };
      dic = JSON.stringify(dic);
      thriftClient.test1(dic, (error, res) => {
        if (error) {
          console.error(error);
        } else {
          this.cmdResult += res;
        }
      });
    }
  }
};
</script>
