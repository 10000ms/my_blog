<template>
    <div class="height-min-height-div thin-content-div">
        <span class="content-title-items">选择父类型</span>
        <div class="child-input-div">
            <i-select v-model="selectCategories" class="max-width" :clearable="true" size="large">
                <i-option v-for="c in categories" :value="c.id" :key="c.id">{{ c.title }}</i-option>
            </i-select>
        </div>
        <span class="content-title-items">类型</span>
        <div class="child-input-div">
            <i-input v-model="category" placeholder="请输入标签..." size="large" style="width: 100%"/>
        </div>
        <div class="child-input-div">
            <Button type="success" long @click="submit" size="large">提交</Button>
        </div>
    </div>
</template>

<script>
    import message from '../../utils/message';

    export default {
        name: 'CategoryOperation',

        data() {
            return {
                id: null,
                category: '',
                selectCategories: null,
                categories: [],
                mode: 'create',
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$api.category()
                    .then(res => {
                        this.categories = res.data;
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
                // 如果是修改模式
                if (this.$route.params.mode && this.$route.params.mode === 'change') {
                    this.id = this.$route.query.id;
                    this.mode = this.$route.params.mode;
                    this.$api.category(this.id)
                        .then(res => {
                            if (res.data.father_category) {
                                this.selectCategories = res.data.father_category.id;
                            }
                            this.category = res.data.title;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                } else {
                    this.mode = 'create';
                    this.id = null;
                    this.category = '';
                    this.selectCategories = null;
                }
            },

            createSubmit() {
                let d = {
                    title: this.category,
                    father_category_pk: this.selectCategories,
                };
                this.$api.createCategory(d)
                    .then(res => {
                        this.$Message.info('添加成功');
                        this.$router.push({name: 'change-category', params: {mode: 'change'}, query: {id: res.data.id}});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            changeSubmit() {
                let d = {
                    title: this.category,
                    father_category_pk: this.selectCategories,
                };
                this.$api.changeCategory(this.id, d)
                    .then(() => {
                        this.$Message.info('修改成功');
                        this.$router.push({name: 'change-category', params: {mode: 'change'}, query: {id: this.id}});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            submit() {
                if (this.mode === 'create') {
                    this.createSubmit();
                } else if (this.mode === 'change') {
                    this.changeSubmit();
                }
            },
        },

        watch: {
            /**
             * 地址改变的时候重新初始化
             */
            '$route'() {
                this.init()
            },
        },

    }
</script>

<style scoped>
    .child-input-div {
        width: 50%;
    }
</style>
