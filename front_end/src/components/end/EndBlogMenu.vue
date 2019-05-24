<template>
    <div>
        <Menu mode="horizontal" active-name="1" class="iview-ui-menu" @on-select="selectMethod">
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
            <div class="menu-right-div">
                <Dropdown trigger="click" @on-click="handleClick">
                    <a href="#">
                        <Avatar icon="md-person" :style="avatarStyle" size="large" :src="profile"/>
                    </a>
                    <DropdownMenu slot="list">
                        <div>
                            <DropdownItem :disabled="true">
                                <span class="dropdown-item color-common-white-items">
                                    欢迎：{{getFullName}}
                                </span>
                            </DropdownItem>
                            <DropdownItem name="user-center">
                                <span class="dropdown-item color-common-white-items">
                                    个人中心
                                </span>
                            </DropdownItem>
                            <DropdownItem name="index">
                                <span class="dropdown-item color-common-white-items">
                                    返回首页
                                </span>
                            </DropdownItem>
                            <DropdownItem name="logout">
                                <span class="dropdown-item color-common-white-items">
                                    退出登录
                                </span>
                            </DropdownItem>
                        </div>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </Menu>
        <user-center ref="UserCenterModel"></user-center>
    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';

    import message from '../../utils/message';

    import UserCenter from '../main/UserCenter';

    export default {
        name: 'BlogMenu',

        components: {
            UserCenter,
        },

        data() {
            return {
                avatarStyle: {
                    'background-color': 'rgba(235, 150, 72, 0.7)',
                    'color': 'rgba(255, 255, 255, 1)',
                },
            };
        },

        methods: {
            handleClick(name) {
                switch (name) {
                    case 'index':
                        this.$router.push({name: 'index'});
                        break;
                    case 'logout':
                        this.logout();
                        break;
                    case 'user-center':
                        this.$refs.UserCenterModel.openModal();
                        break;
                }
            },

            logout() {
                this.$api.logout()
                    .then(() => {
                        this.$store.commit('auth/commitInit', []);
                        this.$Message.info('已退出登录');
                        this.$router.push({name: 'index'});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            selectMethod(key) {
                // 換頁
                this.$router.push({name: key});
            },
        },

        computed: {
            ...mapState('auth', {
                userId: state => state.id,
                profile: state => state.profile,
            }),

            ...mapGetters('auth', [
                'getFullName',
            ]),
        },
    }
</script>

<style scoped>

</style>
