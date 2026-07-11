import pack


def main():
    try:
        pack.install_packages()
    except:
        pass
    from modules.signin import SignIn
    app = SignIn()
    app.mainloop()


if __name__ == "__main__":
    main()
