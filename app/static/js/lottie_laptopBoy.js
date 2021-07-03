LottieInteractivity.create({
    mode:"scroll",
    player: "#thirdLottie" ,
    actions: [
        {
            visibility:[0,0.3],
            type: "stop",
            frames: [0]
        },
        {
        visibility: [0.3,1],
            type: "seek",
            frames: [0, 600]
        }
    ]
});