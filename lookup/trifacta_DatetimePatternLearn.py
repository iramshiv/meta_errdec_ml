"https://docs.trifacta.com/display/ss/Datetime%20Data%20Type?preview=/109906578/154079494/DatetimeFormats.pdf"
from Err_Detect.pattern_Learner import learn_patterns

explicit_date_pattern = ['November 8 2019 13:54-08:00', 'November 8 2019 13:54', 'November 8 2019 1:54 PM-08:00',
                         'November 8 2019 1:54 PM', 'November 8 2019 13:54:55-08:00', 'November 8 2019 13:54:55',
                         'November 8 2019 1:54:55 PM-08:00', 'November 8 2019 1:54:55 PM',
                         'November 8 2019 13:54:55.792-08:00',
                         'November 8 2019 13:54:55.792', 'November 8 2019 1:54:55.792 PM-08:00',
                         'November 8 2019 1:54:55.793 PM',
                         'Nov 8 2019 13:54-08:00', 'Nov 8 2019 13:54', 'Nov 8 2019 1:54 PM-08:00', 'Nov 8 2019 1:54 PM',
                         'Nov 8 2019 13:54:55-08:00', 'Nov 8 2019 13:54:55', 'Nov 8 2019 1:54:55 PM-08:00',
                         'Nov 8 2019 1:54:55 PM',
                         'Nov 8 2019 13:54:55.794-08:00', 'Nov 8 2019 13:54:55.794', 'Nov 8 2019 1:54:55.794 PM-08:00',
                         'Nov 8 2019 1:54:55.794 PM',
                         '1182019 13:54-08:00', '1182019 13:54', '1182019 1:54 PM-08:00', '1182019 1:54 PM',
                         '1182019 13:54:55-08:00',
                         '1182019 13:54:55', '1182019 1:54:55 PM-08:00', '1182019 1:54:55 PM',
                         '1182019 13:54:55.796-08:00', '1182019 13:54:55.796',
                         '1182019 1:54:55.796 PM-08:00', '1182019 1:54:55.796 PM', "11/8/2019 13:54-08:00",
                         "11/8/2019 13:54", "11/8/2019 1:54 PM-08:00",
                         "11/8/2019 1:54 PM", "11/8/2019 13:54:55-08:00", '11/8/2019 13:54:55',
                         '11/8/2019 1:54:55 PM-08:00', '11/8/2019 1:54:55 PM',
                         '11/8/2019 13:54:55.797-08:00', '11/8/2019 13:54:55.797', '11/8/2019 1:54:55.797 PM-08:00',
                         '11/8/2019 1:54:55.798 PM',
                         '11082019 13:54', '11082019 1:54 PM-08:00', '11082019 1:54 PM', '11082019 13:54:55-08:00',
                         '11082019 13:54:55',
                         '11082019 1:54:55 PM-08:00', '11082019 1:54:55 PM', '11082019 13:54:55.796-08:00',
                         '11082019 13:54:55.796',
                         '11082019 1:54:55.796 PM-08:00', '11082019 1:54:55.796 PM', '11/08/2019 13:54-08:00',
                         '11/08/2019 13:54',
                         '11/08/2019 1:54 PM-08:00', '11/08/2019 1:54 PM', '11/08/2019 13:54:55-08:00',
                         '11/08/2019 13:54:55', '11/08/2019 1:54:55 PM-08:00', '11/08/2019 1:54:55 PM',
                         '11/08/2019 13:54:55.797-08:00',
                         '11/08/2019 13:54:55.797', '11/08/2019 1:54:55.797 PM-08:00', '11/08/2019 1:54:55.798 PM',
                         'November 8 19 13:54-08:00',
                         'November 8 19 13:54', 'November 8 19 1:54 PM-08:00', 'November 8 19 1:54 PM',
                         'November 8 19 13:54:55-08:00',
                         'November 8 19 13:54:55', 'November 8 19 1:54:55 PM-08:00', 'November 8 19 1:54:55 PM',
                         'November 8 19 13:54:55.799-08:00',
                         'November 8 19 13:54:55.799', 'November 8 19 1:54:55.799 PM-08:00',
                         'November 8 19 1:54:55.799 PM', 'Nov 8 19 13:54-08:00',
                         'Nov 8 19 13:54', 'Nov 8 19 1:54 PM-08:00', 'Nov 8 19 1:54 PM', 'Nov 8 19 13:54:55-08:00',
                         'Nov 8 19 13:54:55',
                         'Nov 8 19 1:54:55 PM-08:00', 'Nov 8 19 1:54:55 PM', 'Nov 8 19 13:54:55.800-08:00',
                         'Nov 8 19 13:54:55.801',
                         'Nov 8 19 1:54:55.801 PM-08:00', 'Nov 8 19 1:54:55.801 PM', 'November 08 19 13:54-08:00',
                         'November 08 19 13:54',
                         'November 08 19 1:54 PM-08:00', 'November 08 19 1:54 PM', 'November 08 19 13:54:55-08:00',
                         'November 08 19 13:54:55',
                         'November 08 19 1:54:55 PM-08:00', 'November 08 19 1:54:55 PM',
                         'November 08 19 13:54:55.799-08:00',
                         'November 08 19 13:54:55.799', 'November 08 19 1:54:55.799 PM-08:00',
                         'November 08 19 1:54:55.799 PM',
                         'Nov 08 19 13:54-08:00', 'Nov 08 19 13:54', 'Nov 08 19 1:54 PM-08:00', 'Nov 08 19 1:54 PM',
                         'Nov 08 19 13:54:55-08:00',
                         'Nov 08 19 13:54:55', 'Nov 08 19 1:54:55 PM-08:00s', 'Nov 08 19 1:54:55 PM',
                         'Nov 08 19 13:54:55.800-08:00',
                         'Nov 08 19 13:54:55.801', 'Nov 08 19 1:54:55.801 PM-08:00', 'Nov 08 19 1:54:55.801 PM',
                         '11/8/19 13:54-08:00',
                         '11/8/19 13:54', '11/8/19 1:54 PM-08:00', '11/8/19 1:54 PM', '11/8/19 13:54:55-08:00',
                         '11/8/19 13:54:55',
                         '11/8/19 1:54:55 PM-08:00', '11/8/19 1:54:55 PM', '11/8/19 13:54:55.802-08:00',
                         '11/8/19 13:54:55.802',
                         '11/8/19 1:54:55.802 PM-08:00', '11/8/19 1:54:55.803 PM', '11/08/19 13:54-08:00',
                         '11/08/19 13:54',
                         '11/08/19 1:54 PM-08:00', '11/08/19 1:54 PM', '11/08/19 13:54:55-08:00', '11/08/19 13:54:55',
                         '11/08/19 1:54:55 PM-08:00', '11/08/19 1:54:55 PM', '11/08/19 13:54:55.802-08:00',
                         '11/08/19 13:54:55.802',
                         '11/08/19 1:54:55.802 PM-08:00', '11/08/19 1:54:55.803 PM', '8 November 2019 13:54-08:00',
                         '8 November 2019 13:54',
                         '8 November 2019 1:54 PM-08:00', '8 November 2019 1:54 PM', '8 November 2019 13:54:55-08:00',
                         '8 November 2019 13:54:55',
                         '8 November 2019 1:54:55 PM-08:00', '8 November 2019 1:54:55 PM',
                         '8 November 2019 13:54:55.804-08:00',
                         '8 November 2019 13:54:55.804', '8 November 2019 1:54:55.804 PM-08:00',
                         '8 November 2019 1:54:55.804 PM',
                         '8 Nov 2019 13:54-08:00', '8 Nov 2019 13:54', '8 Nov 2019 1:54 PM-08:00', '8 Nov 2019 1:54 PM',
                         '8 Nov 2019 13:54:55-08:00', '8 Nov 2019 13:54:55', '8 Nov 2019 1:54:55 PM-08:00',
                         '8 Nov 2019 1:54:55 PM',
                         '8 Nov 2019 13:54:55.806-08:00', '8 Nov 2019 13:54:55.806', '8 Nov 2019 1:54:55.806 PM-08:00',
                         '8 Nov 2019 1:54:55.806 PM',
                         '08 November 2019 13:54-08:00', '08 November 2019 13:54', '08 November 2019 1:54 PM-08:00',
                         '08 November 2019 1:54 PM',
                         '08 November 2019 13:54:55-08:00', '08 November 2019 13:54:55',
                         '08 November 2019 1:54:55 PM-08:00',
                         '08 November 2019 1:54:55 PM', '08 November 2019 13:54:55.804-08:00',
                         '08 November 2019 13:54:55.804',
                         '08 November 2019 1:54:55.804 PM-08:00', '08 November 2019 1:54:55.804 PM',
                         '08 Nov 2019 13:54-08:00',
                         '08 Nov 2019 13:54', '08 Nov 2019 1:54 PM-08:00', '08 Nov 2019 1:54 PM',
                         '08 Nov 2019 13:54:55-08:00',
                         '08 Nov 2019 13:54:55', '08 Nov 2019 1:54:55 PM-08:00', '08 Nov 2019 1:54:55 PM',
                         '08 Nov 2019 13:54:55.806-08:00',
                         '08 Nov 2019 13:54:55.806', '08 Nov 2019 1:54:55.806 PM-08:00', '08 Nov 2019 1:54:55.806 PM',
                         '8/11/2019 13:54-08:00',
                         '8/11/2019 13:54', '8/11/2019 1:54 PM-08:00', '8/11/2019 1:54 PM', '8/11/2019 13:54:55-08:00',
                         '8/11/2019 13:54:55',
                         '8/11/2019 1:54:55 PM-08:00', '8/11/2019 1:54:55 PM', '8/11/2019 13:54:55.807-08:00',
                         '8/11/2019 13:54:55.807',
                         '8/11/2019 1:54:55.807 PM-08:00', '8/11/2019 1:54:55.808 PM', '08/11/2019 13:54-08:00',
                         '08/11/2019 13:54',
                         '08/11/2019 1:54 PM-08:00', '08/11/2019 1:54 PM', '08/11/2019 13:54:55-08:00',
                         '08/11/2019 13:54:55',
                         '08/11/2019 1:54:55 PM-08:00', '08/11/2019 1:54:55 PM', '08/11/2019 13:54:55.807-08:00',
                         '08/11/2019 13:54:55.807',
                         '08/11/2019 1:54:55.807 PM-08:00', '08/11/2019 1:54:55.808 PM', '8 November 19 13:54-08:00',
                         '8 November 19 13:54',
                         '8 November 19 1:54 PM-08:00', '8 November 19 1:54 PM', '8 November 19 13:54:55-08:00',
                         '8 November 19 13:54:55',
                         '8 November 19 1:54:55 PM-08:00', '8 November 19 1:54:55 PM',
                         '8 November 19 13:54:55.809-08:00',
                         '8 November 19 13:54:55.809', '8 November 19 1:54:55.809 PM-08:00',
                         '8 November 19 1:54:55.809 PM',
                         '8 Nov 19 13:54-08:00', '8 Nov 19 13:54', '8 Nov 19 1:54 PM-08:00', '8 Nov 19 1:54 PM',
                         '8 Nov 19 13:54:55-08:00',
                         '8 Nov 19 13:54:55', '8 Nov 19 1:54:55 PM-08:00', '8 Nov 19 1:54:55 PM',
                         '8 Nov 19 13:54:55.810-08:00',
                         '8 Nov 19 13:54:55.810', '8 Nov 19 1:54:55.811 PM-08:00', '8 Nov 19 1:54:55.811 PM',
                         '08 November 19 13:54-08:00',
                         '08 November 19 13:54', '08 November 19 1:54 PM-08:00', '08 November 19 1:54 PM',
                         '08 November 19 13:54:55-08:00',
                         '08 November 19 13:54:55', '08 November 19 1:54:55 PM-08:00', '08 November 19 1:54:55 PM',
                         '08 November 19 13:54:55.809-08:00', '08 November 19 13:54:55.809',
                         '08 November 19 1:54:55.809 PM-08:00',
                         '08 November 19 1:54:55.809 PM', '08 Nov 19 13:54-08:00', '08 Nov 19 13:54',
                         '08 Nov 19 1:54 PM-08:00',
                         '08 Nov 19 1:54 PM', '08 Nov 19 13:54:55-08:00', '08 Nov 19 13:54:55',
                         '08 Nov 19 1:54:55 PM-08:00',
                         '08 Nov 19 1:54:55 PM', '08 Nov 19 13:54:55.810-08:00', '08 Nov 19 13:54:55.810',
                         '08 Nov 19 1:54:55.811 PM-08:00',
                         '08 Nov 19 1:54:55.811 PM', '8/11/19 13:54-08:00', '8/11/19 13:54', '8/11/19 1:54 PM-08:00',
                         '8/11/19 1:54 PM',
                         '8/11/19 13:54:55-08:00', '8/11/19 13:54:55', '8/11/19 1:54:55 PM-08:00', '8/11/19 1:54:55 PM',
                         '8/11/19 13:54:55.812-08:00', '8/11/19 13:54:55.812', '8/11/19 1:54:55.812 PM-08:00',
                         '8/11/19 1:54:55.813 PM',
                         '08/11/19 13:54-08:00', '08/11/19 13:54', '08/11/19 1:54 PM-08:00', '08/11/19 1:54 PM',
                         '08/11/19 13:54:55-08:00',
                         '08/11/19 13:54:55', '08/11/19 1:54:55 PM-08:00', '08/11/19 1:54:55 PM',
                         '08/11/19 13:54:55.812-08:00',
                         '08/11/19 13:54:55.812', '08/11/19 1:54:55.812 PM-08:00', '08/11/19 1:54:55.813 PM',
                         'November 8 13:54-08:00',
                         'November 8 13:54', 'November 8 1:54 PM-08:00', 'November 8 1:54 PM',
                         'November 8 13:54:55-08:00',
                         'November 8 13:54:55', 'November 8 1:54:55 PM-08:00', 'November 8 1:54:55 PM',
                         'November 8 13:54:55.814-08:00',
                         'November 8 13:54:55.814', 'November 8 1:54:55.814 PM-08:00', 'November 8 1:54:55.814 PM',
                         'Nov 8 13:54-08:00',
                         'Nov 8 13:54', 'Nov 8 1:54 PM-08:00', 'Nov 8 1:54 PM', 'Nov 8 13:54:55-08:00',
                         'Nov 8 13:54:55', 'Nov 8 1:54:55 PM-08:00',
                         'Nov 8 1:54:55 PM', 'Nov 8 13:54:55.815-08:00', 'Nov 8 13:54:55.816',
                         'Nov 8 1:54:55.816 PM-08:00', 'Nov 8 1:54:55.816 PM',
                         'November 08 13:54-08:00', 'November 08 13:54', 'November 08 1:54 PM-08:00',
                         'November 08 1:54 PM',
                         'November 08 13:54:55-08:00', 'November 08 13:54:55', 'November 08 1:54:55 PM-08:00',
                         'November 08 1:54:55 PM',
                         'November 08 13:54:55.814-08:00', 'November 08 13:54:55.814',
                         'November 08 1:54:55.814 PM-08:00',
                         'November 08 1:54:55.814 PM', 'Nov 08 13:54-08:00', 'Nov 08 13:54', 'Nov 08 1:54 PM-08:00',
                         'Nov 08 1:54 PM',
                         'Nov 08 13:54:55-08:00', 'Nov 08 13:54:55', 'Nov 08 1:54:55 PM-08:00', 'Nov 08 1:54:55 PM',
                         'Nov 08 13:54:55.815-08:00',
                         'Nov 08 13:54:55.816', 'Nov 08 1:54:55.816 PM-08:00', 'Nov 08 1:54:55.816 PM',
                         '11/8 13:54-08:00', '11/8 13:54',
                         '11/8 1:54 PM-08:00', '11/8 1:54 PM', '11/8 13:54:55-08:00', '11/8 13:54:55',
                         '11/8 1:54:55 PM-08:00',
                         '11/8 1:54:55 PM', '11/8 13:54:55.817-08:00', '11/8 13:54:55.817', '11/8 1:54:55.818 PM-08:00',
                         '11/8 1:54:55.818 PM',
                         '11/08 13:54-08:00', '11/08 13:54', '11/08 1:54 PM-08:00', '11/08 1:54 PM',
                         '11/08 13:54:55-08:00',
                         '11/08 13:54:55', '11/08 1:54:55 PM-08:00', '11/08 1:54:55 PM', '11/08 13:54:55.817-08:00',
                         '11/08 13:54:55.817',
                         '11/08 1:54:55.818 PM-08:00', '11/08 1:54:55.818 PM', '8 November 13:54-08:00',
                         '8 November 13:54',
                         '8 November 1:54 PM-08:00', '8 November 1:54 PM', '8 November 13:54:55-08:00',
                         '8 November 13:54:55',
                         '8 November 1:54:55 PM-08:00', '8 November 1:54:55 PM', '8 November 13:54:55.819-08:00',
                         '8 November 13:54:55.819',
                         '8 November 1:54:55.819 PM-08:00', '8 November 1:54:55.820 PM', '8 Nov 13:54-08:00',
                         '8 Nov 13:54',
                         '8 Nov 1:54 PM-08:00', '8 Nov 1:54 PM', '8 Nov 13:54:55-08:00', '8 Nov 13:54:55',
                         '8 Nov 1:54:55 PM-08:00',
                         '8 Nov 1:54:55 PM', '8 Nov 13:54:55.821-08:00', '8 Nov 13:54:55.821',
                         '8 Nov 1:54:55.821 PM-08:00',
                         '8 Nov 1:54:55.822 PM', '08 November 13:54-08:00', '08 November 13:54',
                         '08 November 1:54 PM-08:00',
                         '08 November 1:54 PM', '08 November 13:54:55-08:00', '08 November 13:54:55',
                         '08 November 1:54:55 PM-08:00',
                         '08 November 1:54:55 PM', '08 November 13:54:55.819-08:00', '08 November 13:54:55.819',
                         '08 November 1:54:55.819 PM-08:00',
                         '08 November 1:54:55.820 PM', '08 Nov 13:54-08:00', '08 Nov 13:54', '08 Nov 1:54 PM-08:00',
                         '08 Nov 1:54 PM',
                         '08 Nov 13:54:55-08:00', '08 Nov 13:54:55', '08 Nov 1:54:55 PM-08:00', '08 Nov 1:54:55 PM',
                         '08 Nov 13:54:55.821-08:00',
                         '08 Nov 13:54:55.821', '08 Nov 1:54:55.821 PM-08:00', '08 Nov 1:54:55.822 PM',
                         '8/11 13:54-08:00', '8/11 13:54',
                         '8/11 1:54 PM-08:00', '8/11 1:54 PM', '8/11 13:54:55-08:00', '8/11 13:54:55',
                         '8/11 1:54:55 PM-08:00', '8/11 1:54:55 PM',
                         '8/11 13:54:55.823-08:00', '8/11 13:54:55.823', '8/11 1:54:55.823 PM-08:00',
                         '8/11 1:54:55.823 PM', '08/11 13:54-08:00',
                         '08/11 13:54', '08/11 1:54 PM-08:00', '08/11 1:54 PM', '08/11 13:54:55-08:00',
                         '08/11 13:54:55', '08/11 1:54:55 PM-08:00',
                         '08/11 1:54:55 PM', '08/11 13:54:55.823-08:00', '08/11 13:54:55.823',
                         '08/11 1:54:55.823 PM-08:00', '08/11 1:54:55.823 PM',
                         '2019 8 November 13:54-08:00', '2019 8 November 13:54', '2019 8 November 1:54 PM-08:00',
                         '2019 8 November 1:54 PM',
                         '2019 8 November 13:54:55-08:00', '2019 8 November 13:54:55',
                         '2019 8 November 1:54:55 PM-08:00',
                         '2019 8 November 1:54:55 PM', '2019 8 November 13:54:55.825-08:00',
                         '2019 8 November 13:54:55.825',
                         '2019 8 November 1:54:55.825 PM-08:00', '2019 8 November 1:54:55.826 PM',
                         '2019 8 Nov 13:54-08:00',
                         '2019 8 Nov 13:54', '2019 8 Nov 1:54 PM-08:00', '2019 8 Nov 1:54 PM',
                         '2019 8 Nov 13:54:55-08:00',
                         '2019 8 Nov 13:54:55', '2019 8 Nov 1:54:55 PM-08:00', '2019 8 Nov 1:54:55 PM',
                         '2019 8 Nov 13:54:55.827-08:00',
                         '2019 8 Nov 13:54:55.827', '2019 8 Nov 1:54:55.828 PM-08:00', '2019 8 Nov 1:54:55.828 PM',
                         '2019 08 November 13:54-08:00',
                         '2019 08 November 13:54', '2019 08 November 1:54 PM-08:00', '2019 08 November 1:54 PM',
                         '2019 08 November 13:54:55-08:00',
                         '2019 08 November 13:54:55', '2019 08 November 1:54:55 PM-08:00',
                         '2019 08 November 1:54:55 PM',
                         '2019 08 November 13:54:55.825-08:00', '2019 08 November 13:54:55.825',
                         '2019 08 November 1:54:55.825 PM-08:00',
                         '2019 08 November 1:54:55.826 PM', '2019 08 Nov 13:54-08:00', '2019 08 Nov 13:54',
                         '2019 08 Nov 1:54 PM-08:00',
                         '2019 08 Nov 1:54 PM', '2019 08 Nov 13:54:55-08:00', '2019 08 Nov 13:54:55',
                         '2019 08 Nov 1:54:55 PM-08:00',
                         '2019 08 Nov 1:54:55 PM', '2019 08 Nov 13:54:55.827-08:00', '2019 08 Nov 13:54:55.827',
                         '2019 08 Nov 1:54:55.828 PM-08:00',
                         '2019 08 Nov 1:54:55.828 PM', '2019/8/11 13:54-08:00', '2019/8/11 13:54',
                         '2019/8/11 1:54 PM-08:00', '2019/8/11 1:54 PM',
                         '2019/8/11 13:54:55-08:00', '2019/8/11 13:54:55', '2019/8/11 1:54:55 PM-08:00',
                         '2019/8/11 1:54:55 PM',
                         '2019/8/11 13:54:55.829-08:00', '2019/8/11 13:54:55.830', '2019/8/11 1:54:55.830 PM-08:00',
                         '2019/8/11 1:54:55.830 PM',
                         '2019/08/11 13:54-08:00', '2019/08/11 13:54', '2019/08/11 1:54 PM-08:00', '2019/08/11 1:54 PM',
                         '2019/08/11 13:54:55-08:00',
                         '2019/08/11 13:54:55', '2019/08/11 1:54:55 PM-08:00', '2019/08/11 1:54:55 PM',
                         '2019/08/11 13:54:55.829-08:00',
                         '2019/08/11 13:54:55.830', '2019/08/11 1:54:55.830 PM-08:00', '2019/08/11 1:54:55.830 PM',
                         '2019 November 8 13:54-08:00',
                         '2019 November 8 13:54', '2019 November 8 1:54 PM-08:00', '2019 November 8 1:54 PM',
                         '2019 November 8 13:54:55-08:00',
                         '2019 November 8 13:54:55', '2019 November 8 1:54:55 PM-08:00', '2019 November 8 1:54:55 PM',
                         '2019 November 8 13:54:55.832-08:00', '2019 November 8 13:54:55.832',
                         '2019 November 8 1:54:55.832 PM-08:00',
                         '2019 November 8 1:54:55.832 PM', '2019 Nov 8 13:54-08:00', '2019 Nov 8 13:54',
                         '2019 Nov 8 1:54 PM-08:00',
                         '2019 Nov 8 1:54 PM', '2019 Nov 8 13:54:55-08:00', '2019 Nov 8 13:54:55',
                         '2019 Nov 8 1:54:55 PM-08:00',
                         '2019 Nov 8 1:54:55 PM', '2019 Nov 8 13:54:55.834-08:00', '2019 Nov 8 13:54:55.834',
                         '2019 Nov 8 1:54:55.834 PM-08:00',
                         '2019 Nov 8 1:54:55.835 PM', '2019 November 08 13:54-08:00', '2019 November 08 13:54',
                         '2019 November 08 1:54 PM-08:00',
                         '2019 November 08 1:54 PM', '2019 November 08 13:54:55-08:00', '2019 November 08 13:54:55',
                         '2019 November 08 1:54:55 PM-08:00', '2019 November 08 1:54:55 PM',
                         '2019 November 08 13:54:55.832-08:00',
                         '2019 November 08 13:54:55.832', '2019 November 08 1:54:55.832 PM-08:00',
                         '2019 November 08 1:54:55.832 PM',
                         '2019 Nov 08 13:54-08:00', '2019 Nov 08 13:54', '2019 Nov 08 1:54 PM-08:00',
                         '2019 Nov 08 1:54 PM',
                         '2019 Nov 08 13:54:55-08:00', '2019 Nov 08 13:54:55', '2019 Nov 08 1:54:55 PM-08:00',
                         '2019 Nov 08 1:54:55 PM',
                         '2019 Nov 08 13:54:55.834-08:00', '2019 Nov 08 13:54:55.834',
                         '2019 Nov 08 1:54:55.834 PM-08:00',
                         '2019 Nov 08 1:54:55.835 PM', '2019/11/8 13:54-08:00', '2019/11/8 13:54',
                         '2019/11/8 1:54 PM-08:00',
                         '2019/11/8 1:54 PM', '2019/11/8 13:54:55-08:00', '2019/11/8 13:54:55',
                         '2019/11/8 1:54:55 PM-08:00',
                         '2019/11/8 1:54:55 PM', '2019/11/8 13:54:55.837-08:00', '2019/11/8 13:54:55.837',
                         '2019/11/8 1:54:55.837 PM-08:00',
                         '2019/11/8 1:54:55.837 PM', '2019118 13:54-08:00', '2019118 13:54', '2019118 1:54 PM-08:00',
                         '2019118 1:54 PM',
                         '2019118 13:54:55-08:00', '2019118 13:54:55', '2019118 1:54:55 PM-08:00', '2019118 1:54:55 PM',
                         '2019118 13:54:55.839-08:00', '2019118 13:54:55.839', '2019118 1:54:55.844 PM-08:00',
                         '2019118 1:54:55.845 PM',
                         '19/11/8 13:54-08:00', '19/11/8 13:54', '19/11/8 1:54 PM-08:00', '19/11/8 1:54 PM',
                         '19/11/8 13:54:55-08:00',
                         '19/11/8 13:54:55', '19/11/8 1:54:55 PM-08:00', '19/11/8 1:54:55 PM',
                         '19/11/8 13:54:55.846-08:00',
                         '19/11/8 13:54:55.847', '19/11/8 1:54:55.847 PM-08:00', '19/11/8 1:54:55.847 PM',
                         '2019118135455847-08:00',
                         '2019118135455847', '2019118135455-08:00', '2019118135455', '2019/11/08 13:54-08:00',
                         '2019/11/08 13:54',
                         '2019/11/08 1:54 PM-08:00', '2019/11/08 1:54 PM', '2019/11/08 13:54:55-08:00',
                         '2019/11/08 13:54:55',
                         '2019/11/08 1:54:55 PM-08:00', '2019/11/08 1:54:55 PM', '2019/11/08 13:54:55.837-08:00',
                         '2019/11/08 13:54:55.837',
                         '2019/11/08 1:54:55.837 PM-08:00', '2019/11/08 1:54:55.837 PM', '20191108 13:54-08:00',
                         '20191108 13:54',
                         '20191108 1:54 PM-08:00', '20191108 1:54 PM', '20191108 13:54:55-08:00', '20191108 13:54:55',
                         '20191108 1:54:55 PM-08:00',
                         '20191108 1:54:55 PM', '20191108 13:54:55.839-08:00', '20191108 13:54:55.839',
                         '20191108 1:54:55.844 PM-08:00',
                         '20191108 1:54:55.845 PM', '19/11/08 13:54-08:00', '19/11/08 13:54', '19/11/08 1:54 PM-08:00',
                         '19/11/08 1:54 PM',
                         '19/11/08 13:54:55-08:00', '19/11/08 13:54:55', '19/11/08 1:54:55 PM-08:00',
                         '19/11/08 1:54:55 PM',
                         '19/11/08 13:54:55.846-08:00', '19/11/08 13:54:55.847', '19/11/08 1:54:55.847 PM-08:00',
                         '19/11/08 1:54:55.847 PM',
                         '20191108135455847-08:00', '20191108135455847', '20191108135455-08:00', '20191108135455']

x = learn_patterns(explicit_date_pattern)
print(x)

with open('trifacta_DataTimePattern.txt', 'w') as fp:
    for i in x:
        fp.write("%s\n" % i)
    print('done')
