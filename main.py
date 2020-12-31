import cec

def main():
    cec.init()

    tv = cec.Device(cec.CECDEVICE_TV)

    # 電源が入っているか
    print(tv.is_on())
    # => True / False


    # if tv.is_on():
    #     # 電源がONの場合、次はスタンバイにする
    #     tv.standby()
    # else:
    #     # 電源が入っていない場合、電源を入れる
    #     tv.power_on()

    # ベンダ
    print(tv.vendor)
    # => 000000

    # 言語
    print(tv.language)
    # => ??? (電源ONの場合は、jpn)

    print(tv.osd_string)
    # => TV

    print(tv.cec_version)
    # => 1.4

    # 音量周りは、一度にどちらかだけ
    # 音量を一段階上げる
    # cec.volume_up()
    # 音量を一段階下げる
    cec.volume_down()


if __name__ == '__main__':
    main()
