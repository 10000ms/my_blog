<template>
    <div>
        <Menu mode="horizontal" active-name="1" class="iview-ui-menu" @on-select="selectMethod">
            <MenuItem name="index" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon class="menu-icon" type="ios-home" size="16"/>
                    Index
                </span>
            </MenuItem>
            <MenuItem name="tabs" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon class="menu-icon" type="md-pricetags" size="16"/>
                    Tabs
                </span>
            </MenuItem>
            <MenuItem name="categories" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon class="menu-icon" type="md-filing" size="16"/>
                    Categories
                </span>
            </MenuItem>
            <MenuItem name="archive" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon class="menu-icon" type="md-clock" size="16"/>
                    Archive
                </span>
            </MenuItem>
            <MenuItem name="aboutMe" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon class="menu-icon" type="ios-quote" size="16"/>
                    About Me
                </span>
            </MenuItem>
            <div class="avatar-div content-content-items">
                <Dropdown trigger="click" @on-click="handleClick">
                    <a href="#">
                        <div class="profile-large-icon">
                            <Avatar icon="md-person" :style="avatarStyle" size="large" :src="profile"/>
                        </div>
                        <div class="profile-small-icon">
                            <Avatar icon="md-person" :style="avatarStyle" size="small" :src="profile"/>
                        </div>
                    </a>
                    <DropdownMenu slot="list">
                        <div v-if="! userId">
                            <DropdownItem name="login">
                                <span class="dropdown-item color-common-white-items">
                                    登录
                                </span>
                            </DropdownItem>
                            <DropdownItem name="register" v-show="openRegister">
                                <span class="dropdown-item color-common-white-items">
                                    注册
                                </span>
                            </DropdownItem>
                        </div>
                        <div v-if="userId">
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
                            <DropdownItem name="admin" v-show="isSuperuser">
                                <span class="dropdown-item color-common-white-items">
                                    管理中心
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
        <login ref="loginModel"></login>
        <register ref="registerModel"></register>
        <user-center ref="UserCenterModel"></user-center>
    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';

    import Login from './Login';
    import Register from './Register';
    import UserCenter from '../main/UserCenter';
    import message from '../../utils/message';

    export default {
        name: 'BlogMenu',
        components: {
            Register,
            Login,
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

        computed: {
            ...mapState('auth', {
                userId: state => state.id,
                isSuperuser: state => state.isSuperuser,
                profile: state => state.profile,
            }),
            ...mapState('website', {
                openRegister: state => state.openRegister,
            }),

            ...mapGetters('auth', [
                'getFullName',
            ]),
        },

        methods: {
            handleClick(name) {
                switch (name) {
                    case 'login':
                        this.$refs.loginModel.openModal();
                        break;
                    case 'register':
                        if (this.openRegister) {
                            this.$refs.registerModel.openModal();
                        } else {
                            this.$Message.error('本网站不开放注册')
                        }
                        break;
                    case 'admin':
                        this.$router.push({name: 'endIndex'});
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
    }
</script>

<style scoped>

</style>
