import React from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

const CustomLayout = (props) => {
    return (
        <Layout className="layout">
            <Header>
                <div className="logo" />
                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={['2']}
                    style={{ lineHeight: '64px' }}
                >
                    {
                        props.isAuthenticated ?

                            <Menu.Item key="2">
                                LogOut
                            </Menu.Item>

                            :

                            <Menu.Item key="2">
                                <Link to="/login">LogIn</Link>
                            </Menu.Item>

                    }

                    <Menu.Item key="1">
                        <Link to="/">Main</Link>
                    </Menu.Item>

                    <Menu.Item key="3">
                        <Link to="/login">Login</Link>
                    </Menu.Item>
                </Menu>
            </Header>
            <Content style={{ padding: '0 50px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item><Link to="/">Home</Link></Breadcrumb.Item>
                    <Breadcrumb.Item><Link to="/">Announcement</Link></Breadcrumb.Item>
                </Breadcrumb>
                <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                    {props.children}
                </div>
            </Content>
            <Footer style={{ textAlign: 'center' }}>
                BSUiR ©2020 Created by Studenthood LI
            </Footer>
        </Layout>
    );
}

export default CustomLayout;