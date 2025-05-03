pub enum CurrentScreen {
    Main,
    Settings,
    EditingSettings,
}

pub enum EditingSettings {
    Key,
    Value,
}

#[derive(Clone, Debug)]
pub struct Message {
    sender: String,
    text: String,
}
