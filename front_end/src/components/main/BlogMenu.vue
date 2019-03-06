<template>
  <div>
    <Menu mode="horizontal" active-name="1" :style="menuStyle" @on-select="selectMethod">
      <MenuItem name="index" class="menu-menu">
    <span class="span-menu">
      <Icon type="ios-home" size="16"/>
      Index
    </span>
      </MenuItem>
      <MenuItem name="tabs" class="menu-menu">
    <span class="span-menu">
      <Icon type="md-pricetags" size="16"/>
      Tabs
    </span>
      </MenuItem>
      <MenuItem name="categories" class="menu-menu">
    <span class="span-menu">
      <Icon type="md-filing" size="16"/>
      Categories
    </span>
      </MenuItem>
      <MenuItem name="archive" class="menu-menu">
    <span class="span-menu">
      <Icon type="md-clock" size="16"/>
      Archive
    </span>
      </MenuItem>
      <MenuItem name="aboutMe" class="menu-menu">
    <span class="span-menu">
      <Icon type="ios-quote" size="16"/>
      About Me
    </span>
      </MenuItem>
      <div class="avatar-div">
        <Dropdown trigger="click" @on-click="handleClick">
          <a href="#">
            <Avatar icon="md-person" :style="avatarStyle" size="large" :src="avatarURL"/>
          </a>
          <DropdownMenu slot="list">
            <div v-if="!userName">
              <DropdownItem name="login">
                <span class="dropdown-item">
                  登录
                </span>
              </DropdownItem>
              <DropdownItem name="register">
                <span class="dropdown-item">
                  注册
                </span>
              </DropdownItem>
            </div>
            <div v-if="userName">
              <DropdownItem disabled="true">
                <span class="dropdown-item">
                  欢迎：{{userName}}
                </span>
              </DropdownItem>
              <DropdownItem name="admin">
                <span class="dropdown-item">
                  管理中心
                </span>
              </DropdownItem>
              <DropdownItem>
                <span class="dropdown-item">
                  退出登录
                </span>
              </DropdownItem>
            </div>
          </DropdownMenu>
        </Dropdown>
      </div>
    </Menu>
    <login ref="loginModel"></login>
    <register ref="registerModel"></register>
  </div>
</template>

<script>
    import Login from './Login'
    import Register from './Register'

    export default {
        name: 'BlogMenu',
        components: {Register, Login},

        data() {
            return {
                menuStyle: {
                    'background-image': 'linear-gradient(to left,#cc2b5e,#753a88)',
                    'height': '65px',
                },
                avatarStyle: {
                    'background-color': 'rgba(235, 150, 72, 0.7)',
                    'color': 'rgba(255, 255, 255, 1)',
                },
                // TODO： 放入vuex
                userName: 123456,
                avatarURL: null,
            }
        },

        methods: {
            handleClick(name) {
                switch (name) {
                    case 'login':
                        this.$refs.loginModel.openModal();
                        break;
                    case 'register':
                        this.$refs.registerModel.openModal();
                        break;
                    case 'admin':
                        this.$router.push({name: 'adminIndex'});
                        break;
                }
            },
            selectMethod(key) {
                // 換頁
                this.$router.push({name: key});
            },

        },
    }
</script>

<style scoped>
  .menu-menu {
    font-size: 15px;
    cursor: pointer;

  }

  .menu-menu {
    color: rgba(255, 255, 255, 0.7) !important;
  }

  .menu-menu:hover {
    color: rgb(45, 140, 240) !important;
    font-size: 16px;
  }

  .avatar-div {
    float: right;
    margin-right: 50px;
    font-size: 16px;
  }

  .dropdown-item {
    font-size: 14px;
    padding: 5px;
    color: #fff;
  }

  /*选中菜单颜色*/
  .ivu-menu-item-active {
    color: rgba(255, 255, 255, 1) !important;
    font-size: 16px;
    font-weight: 600;
  }
</style>

<style>
  /*登录dropdown配色更改*/
  .ivu-select-dropdown {
    background: linear-gradient(to left, #cc2b5e, #753a88) !important;
    color: white;
  }

  .ivu-menu-item:hover {
    background: none !important;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .2);
  }

  .ivu-dropdown-item:hover {
    background: inherit !important;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .2);
  }
</style>
