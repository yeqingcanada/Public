<ToggleDiv name="- Toggle Buttons -">
    <>
        {buttonGroup.map((button) => (
            <React.Fragment key={`fragment-${button.id}`}>
                <Button
                    className={`m-2 ${button.type}`}
                    onClick={() => button.handleClick(selectedRowID)}
                    key={`button-${button.buttonText}`}
                >
                    {button.buttonText}
                </Button>
            </React.Fragment>
        ))}
    </>
</ToggleDiv>