<template>
    <div>
        <Menu mode="horizontal" active-name="1" :style="menuStyle" @on-select="selectMethod">
            <MenuItem name="endIndex" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon type="ios-speedometer" size="16"/>
                    总览
                </span>
            </MenuItem>
            <Submenu name="1" class="menu-menu content-content-items">
                <template slot="title">
                  <span class="span-menu">
                      <Icon type="ios-home" size="16"/>
                      文章管理
                  </span>
                </template>
                <MenuItem name="create-blog">
                    <span class="dropdown-item color-common-white-items">
                    新文章
                  </span>
                </MenuItem>
                <MenuItem name="manage-blog">
                    <span class="dropdown-item color-common-white-items">
                        所有文章
                    </span>
                </MenuItem>
            </Submenu>
            <Submenu name="2" class="menu-menu content-content-items">
                <template slot="title">
                    <span class="span-menu">
                        <Icon type="md-pricetags" size="16"/>
                        标签管理
                    </span>
                </template>
                <MenuItem name="create-tab">
                    <span class="dropdown-item color-common-white-items">
                        新标签
                    </span>
                </MenuItem>
                <MenuItem name="manage-tabs">
                    <span class="dropdown-item color-common-white-items">
                        所有标签
                    </span>
                </MenuItem>
            </Submenu>
            <Submenu name="3" class="menu-menu content-content-items">
                <template slot="title">
                    <span class="span-menu">
                        <Icon type="md-filing" size="16"/>
                        类型管理
                    </span>
                </template>
                <MenuItem name="create-category">
                    <span class="dropdown-item color-common-white-items">
                        新类型
                    </span>
                </MenuItem>
                <MenuItem name="manage-categories">
                    <span class="dropdown-item color-common-white-items">
                        所有类型
                    </span>
                </MenuItem>
            </Submenu>
            <MenuItem name="end-about-me" class="menu-menu content-content-items">
                <span class="span-menu">
                  <Icon type="ios-quote" size="16"/>
                  个人简介管理
                </span>
            </MenuItem>
            <MenuItem name="manage-website" class="menu-menu content-content-items">
                <span class="span-menu">
                  <Icon type="md-bulb" size="16"/>
                  网站管理
                </span>
            </MenuItem>
            <div class="avatar-div">
                <Dropdown trigger="click" @on-click="handleClick">
                    <a href="#">
                        <Avatar icon="md-person" :style="avatarStyle" size="large" :src="avatarURL"/>
                    </a>
                    <DropdownMenu slot="list">
                        <div>
                            <DropdownItem :disabled="true">
                                <span class="dropdown-item color-common-white-items">
                                    欢迎：{{userName}}
                                </span>
                            </DropdownItem>
                            <DropdownItem name="index">
                                <span class="dropdown-item color-common-white-items">
                                    返回首页
                                </span>
                            </DropdownItem>
                            <DropdownItem>
                                <span class="dropdown-item color-common-white-items">
                                    退出登录
                                </span>
                            </DropdownItem>
                        </div>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </Menu>
    </div>
</template>

<script>

    export default {
        name: 'BlogMenu',

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
            };
        },

        methods: {
            handleClick(name) {
                switch (name) {
                    case 'index':
                        this.$router.push({name: 'index'});
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

</style>
