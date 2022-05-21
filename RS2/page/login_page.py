from RS2.base.base_page import BasePage


class LoginPage(BasePage):
    # 属性
    tiaoguo_loc = 'c=count-down'  #跳过
    yuyan_loc = 'c=lang'   #语言
    zhongwen_loc = 'c=lang-list-item'   #中文
    loginin_loc = 'c=login-btn'  #登录
    register_loc = 'c=register-btn'  #注册
    user_loc = 'c=uni-input-input'  # 输入帐号或邮箱
    #输入验证码
    yzm_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input'
    #输入邮箱验证码
    yxyzm_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[4]/uni-input/div/input'
    pwd_loc = 'x=//*[@type="password"]'  #输入密码
    login_loc = 'c=btn'  #点击登录
    jinru_loc = 'c=enter-btn'  #注册完进入
    assert_loc = 'c=uni-sample-toast'  #断言信息
    shouye_loc = 'x=/html/body/uni-app/uni-tabbar/div[1]/div[2]/div/div[1]/img'  #首页
    xiaoxi_loc = 'x=/html/body/uni-app/uni-tabbar/div[1]/div[3]/div/div[1]/img'  #消息
    shipin_loc = 'x=/html/body/uni-app/uni-tabbar/div[1]/div[4]/div/div[1]/img'  #视频
    wodeye_loc = 'x=/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img'  #我的
    #搜索
    sousuo_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]/uni-view[2]/uni-view[2]/uni-image/img'
    #点击搜索后的用户图像
    tuxiang_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view/uni-view[1]/uni-image/img'
    #个人主页点礼物
    liwu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-image[1]/img'
    #选中礼物
    xuanliwu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view/uni-view[2]/uni-view/uni-view/uni-view/uni-view[2]/uni-swiper/div/div[1]/div/uni-swiper-item[1]/uni-view/uni-view[2]/uni-view/uni-image/img'
    #收起
    shouqi_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]/uni-image/img'
    #聊天
    liaotian_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-image[3]/img'
    #发送消息
    faxiaoxi_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view/uni-view[2]/uni-image/img'
    #聊天对话框点礼物
    lliwu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-view[3]/uni-image/img'
    #选中礼物
    lxliwu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view/uni-view[2]/uni-view/uni-view/uni-view/uni-view[2]/uni-swiper/div/div[1]/div/uni-swiper-item[1]/uni-view/uni-view[1]/uni-view/uni-image/img'
    #表情
    biaoqing_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[1]/uni-view[1]/uni-image/img'
    #选表情
    xbiaoqing_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-swiper/div/div[1]/div/uni-swiper-item[1]/uni-view[1]/uni-view[3]/uni-image/img'
    #赠送
    zengsong_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view/uni-view[2]/uni-view/uni-view/uni-view/uni-view[3]/uni-view[2]/uni-view'
    #返回
    fanhui_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-image[1]/img'
    #返回1
    fanhui1_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-image[1]/img'
    #取消
    back_loc = 'c=back'
    #消息列表聊天
    xxtuxiang_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[5]/uni-view[1]/uni-view[1]/uni-view/uni-view[2]/uni-view/uni-image[2]/img'
    #点击一条消息的时间
    xxshijian_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[5]/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view/uni-view/uni-view[1]/uni-view[2]'
    #相册
    xiangce_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-view[1]/uni-image/img'
    #付费发送
    fufeifa_loc = 'x=/html/body/uni-app/uni-modal/div[2]/div[3]/div[2]'

    #翻译
    fanyi_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-view[4]/uni-image/img'
    #日语
    riyu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view/uni-view[2]/uni-view[4]'
    #英文
    yingwen_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view/uni-view[2]/uni-view[3]'
    #法语
    fayu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view/uni-view[2]/uni-view[6]'
    #设置
    shezhi_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img'
    loginout_loc = 'c=login-out'  #退出

    #充值
    chongzhi_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[1]/uni-navigator'
    #冲500
    wubai_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[2]/uni-view[1]/uni-text/span'
    #冲1000
    yiqian_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[3]/uni-view[1]/uni-text/span'
    #冲1500
    yiqianwu_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[4]/uni-view[1]/uni-text/span'
    #冲2000
    liangqian_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[5]/uni-view[1]/uni-text/span'
    #冲自填
    zitian_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[6]/uni-view[1]/uni-view/uni-image/img'
    #填数字
    tianshuzi_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[6]/uni-view[2]/uni-view[1]/uni-view/uni-input/div/input'
    #确定充值
    chong_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[2]/uni-view'
    #K
    K_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[2]/uni-radio-group/uni-view[1]/uni-radio/div/div'
    #N
    N_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[2]/uni-radio-group/uni-view[2]/uni-radio/div/div'
    #G
    G_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[2]/uni-radio-group/uni-view[3]/uni-radio/div/div'
    #W
    W_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[2]/uni-radio-group/uni-view[4]/uni-radio/div/div'
    #V
    V_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[2]/uni-radio-group/uni-view[5]/uni-radio/div/div'
    #关闭窗口1
    chuangkou_loc = 'x=/html/body/uni-app/uni-page/uni-page-head/div[1]/div[1]/div[2]/div/i'
    #返回
    return_loc = 'x=/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]/uni-view/uni-image/img'




    # 方法
    def click_tiaoguo(self):
        self.click(self.tiaoguo_loc)

    def click_yuyan(self):
        self.click(self.yuyan_loc)

    def click_zhongwen(self):
        self.click(self.zhongwen_loc)

    def click_loginin(self):
        self.click(self.loginin_loc)

    def click_register(self):
        self.click(self.register_loc)

    def input_user(self, user):
        self.type(self.user_loc, user)

    def input_yzm(self, yzm):
        self.type(self.yzm_loc, yzm)

    def input_yxyzm(self, yxyzm):
        self.type(self.yxyzm_loc,yxyzm)

    def input_pwd(self, pwd):
        self.type(self.pwd_loc, pwd)

    def click_login(self):
        self.click(self.login_loc)

    def click_jinru(self):
        self.click(self.jinru_loc)

    def get_assert(self):
        return self.get_text(self.assert_loc)

    def click_shouye(self):
        self.click(self.shouye_loc)

    def click_xiaoxi(self):
        self.click(self.xiaoxi_loc)

    def click_shipin(self):
        self.click(self.shipin_loc)

    def click_wodeye(self):
        self.click(self.wodeye_loc)

    def click_sousuo(self):
        self.click(self.sousuo_loc)

    def click_tuxiang(self):
        self.click(self.tuxiang_loc)

    def click_liwu(self):
        self.click(self.liwu_loc)

    def click_xuanliwu(self):
        self.click(self.xuanliwu_loc)

    def click_liaotian(self):
        self.click(self.liaotian_loc)

    def click_faxiaoxi(self):
        self.click(self.faxiaoxi_loc)

    def click_lliwu(self):
        self.click(self.lliwu_loc)

    def click_lxliwu(self):
        self.click(self.lxliwu_loc)

    def click_biaoqing(self):
        self.click(self.biaoqing_loc)

    def click_xbiaoqing(self):
        self.click(self.xbiaoqing_loc)

    def click_zengsong(self):
        self.click(self.zengsong_loc)

    def click_fanhui(self):
        self.click(self.fanhui_loc)

    def click_fanhui1(self):
        self.click(self.fanhui1_loc)

    def click_back(self):
        self.click(self.back_loc)

    def click_xxtuxiang(self):
        self.click(self.xxtuxiang_loc)

    def click_shouqi(self):
        self.click(self.shouqi_loc)

    def click_xxshijain(self):
        self.click(self.xxshijian_loc)

    def click_xiangce(self):
        self.click(self.xiangce_loc)

    def click_fufeifa(self):
        self.click(self.fufeifa_loc)

    def click_fanyi(self):
        self.click(self.fanyi_loc)

    def click_riyu(self):
        self.click(self.riyu_loc)

    def click_fayu(self):
        self.click(self.fayu_loc)

    def click_yingwen(self):
        self.click(self.yingwen_loc)

    def click_shezhi(self):
        self.click(self.shezhi_loc)

    def click_loginout(self):
        self.click(self.loginout_loc)

    def click_chongzhi(self):
        self.click(self.chongzhi_loc)

    def click_wubai(self):
        self.click(self.wubai_loc)

    def click_yiqian(self):
        self.click(self.yiqian_loc)

    def click_yiqianwu(self):
        self.click(self.yiqianwu_loc)

    def click_liangqian(self):
        self.click(self.liangqian_loc)

    def click_zitian(self):
        self.click(self.zitian_loc)

    def input_tianshuzi(self, tianshuzi):
        self.type(self.tianshuzi_loc, tianshuzi)

    def click_chong(self):
        self.click(self.chong_loc)

    def click_K(self):
        self.click(self.K_loc)

    def click_N(self):
        self.click(self.N_loc)

    def click_G(self):
        self.click(self.G_loc)

    def click_W(self):
        self.click(self.W_loc)

    def click_V(self):
        self.click(self.V_loc)

    def click_chuangkou(self):
        self.click(self.chuangkou_loc)

    def click_return(self):
        self.click(self.return_loc)

    def ceshi(self):
        self.open('http://app.ringsmiley.top')
        self.wait(2)
        self.click_tiaoguo()
        self.wait(3)
        self.click_yuyan()
        self.wait(2)
        self.click_zhongwen()
        self.wait(2)

    # def login(self, user='100001181', pwd='123456a'):
    #     yzm = self.Yzm()
    #     self.input_user(user)
    #     self.input_yzm(yzm)
    #     self.input_pwd(pwd)
    #     self.click_login()
    #
    # def register(self, user='5655889@qq.com', yzm='123456', pwd='123456a'):
    #     self.input_user(user)
    #     self.input_yzm(yzm)
    #     self.input_pwd(pwd)
    #     self.click_login()

    # def get_realname(self):
    #     return self.get_text(self.realname_loc)
    #
    # def click_confirm(self):
    #     self.click(self.confirm_loc)
    #
    # def get_failtip(self):
    #     return self.get_text(self.failtip_loc)

    # def login(self, account='admin', password='123456'):
    #     self.input_account(account)
    #     self.input_password(password)
    #     self.click_submit()
