<template>
    <Modal
            v-model="show"
            title="Common Modal dialog box title"
            @on-ok="changeUserData"
            :loading="loading"
            :closable="true"
            scrollable
    >
        <p slot="header" :style="headerStyle">
            <span>个人中心</span>
        </p>
        <div class="thin-content-div text-align-center-div">
            <Avatar icon="md-person" :style="avatarStyle" size="large" :src="profile"/>
        </div>
        <div class="dialog-single-input-div">
            <i-input v-model="profile" placeholder="头像图片URL地址"/>
        </div>
        <div class="dialog-single-input-div" v-if="isSuperuser">
            <span>是否是作者： </span>
            <i-switch v-model="tempIsAuthor" size="large">
                <span slot="open">是</span>
                <span slot="close">否</span>
            </i-switch>
        </div>
    </Modal>
</template>

<script>
    import xss from 'xss';
    import { mapState } from 'vuex';

    import message from '../../utils/message';

    export default {
        name: 'UserCenter',

        data() {
            return {
                show: false,
                headerStyle: {
                    'color': 'rgba(246, 141, 66, 1)',
                    'text-align': 'center',
                    'font-size': '18px',
                    'margin': '5px',
                    'letter-spacing': '20px',
                },
                avatarStyle: {
                    'background-color': 'rgba(235, 150, 72, 0.7)',
                    'color': 'rgba(255, 255, 255, 1)',
                },
                loading: true,
                profile: this.oldProfile ? this.oldProfile : '',
                tempIsAuthor: false,
            };
        },

        methods: {
            openModal() {
                this.show = true;
                this.tempIsAuthor = this.isAuthor;
            },

            changeUserData() {
                if (! this.profile.length) {
                    this.$Message.warning('请输入头像图片URL地址');
                } else {
                    let d = {
                        profile: xss(this.profile),
                        is_author: this.tempIsAuthor,
                    };
                    this.$api.changeUserData(this.userId, d)
                        .then(res => {
                            this.$store.commit('auth/commitInit', res.data);
                            this.$Message.info('修改用户资料成功');
                            this.show = false;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                }
                // 关闭这一轮的loading，并且保证下一轮存在loading
                this.loading = false;
                this.$nextTick(() => {
                    this.loading = true;
                });
            },
        },

        watch: {
            oldProfile() {
                // 头像数据可能是后面传进来的
                this.profile = this.oldProfile;
            }
        },

        computed: {
            ...mapState('auth', {
                userId: state => state.id,
                oldProfile: state => state.profile,
                isAuthor: state => state.isAuthor,
                isSuperuser: state => state.isSuperuser,
            }),
        },
    }
</script>

<style scoped>

</style>