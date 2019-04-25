<template>
    <div>
        <Menu mode="horizontal" active-name="1" :style="menuStyle" @on-select="selectMethod">
            <MenuItem name="index" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon type="ios-home" size="16"/>
                    Index
                </span>
            </MenuItem>
            <MenuItem name="tabs" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon type="md-pricetags" size="16"/>
                    Tabs
                </span>
            </MenuItem>
            <MenuItem name="categories" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon type="md-filing" size="16"/>
                    Categories
                </span>
            </MenuItem>
            <MenuItem name="archive" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon type="md-clock" size="16"/>
                    Archive
                </span>
            </MenuItem>
            <MenuItem name="aboutMe" class="menu-menu content-content-items">
                <span class="span-menu">
                    <Icon type="ios-quote" size="16"/>
                    About Me
                </span>
            </MenuItem>
            <div class="avatar-div content-content-items">
                <Dropdown trigger="click" @on-click="handleClick">
                    <a href="#">
                        <Avatar icon="md-person" :style="avatarStyle" size="large" :src="avatarURL"/>
                    </a>
                    <DropdownMenu slot="list">
                        <div v-if="! userId">
                            <DropdownItem name="login">
                                <span class="dropdown-item color-common-white-items">
                                    登录
                                </span>
                            </DropdownItem>
                            <DropdownItem name="register">
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
                            <DropdownItem name="admin" v-show="isSuperuser">
                                <span class="dropdown-item color-common-white-items">
                                    管理中心
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
        <login ref="loginModel"></login>
        <register ref="registerModel"></register>
    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';

    import Login from './Login';
    import Register from './Register';

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
                // TODO： 增加这个功能
                avatarURL: null,
            };
        },

        computed: {
            ...mapState('auth', {
                userId: state => state.id,
                isSuperuser: state => state.isSuperuser,
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
                        this.$refs.registerModel.openModal();
                        break;
                    case 'admin':
                        this.$router.push({name: 'endIndex'});
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
