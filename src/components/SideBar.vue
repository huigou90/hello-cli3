<template>
  <el-col :span="16" id="sideBar">
    <el-menu router>
      <el-menu-item index="/"><i class="el-icon-menu"></i>主页</el-menu-item>
      <el-menu-item index="/example"
        ><i class="el-icon-edit"></i>例子1</el-menu-item
      >
      <el-menu-item index="/example2"
        ><i class="el-icon-question"></i>例子2</el-menu-item
      >
    </el-menu>
  </el-col>
</template>

<style>
#sideBar {
  height: 100%;
  text-align: left;
}
</style>
