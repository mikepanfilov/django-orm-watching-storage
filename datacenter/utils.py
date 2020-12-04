def format_duration(duration):
    seconds = duration.total_seconds()
    minutes = int((seconds % 3600) // 60)
    hours = int(seconds // 3600)

    least_h_digit = int(str(hours)[-1])
    if least_h_digit == 1:
        h_end = ''
    elif 2 <= least_h_digit <= 4:
        h_end = 'а'
    else:
        h_end = 'ов'

    least_m_digit = int(str(minutes)[-1])
    if least_m_digit == 1:
        m_end = 'а'
    elif 2 <= least_m_digit <= 4:
        m_end = 'ы'
    else:
        m_end = ''
    if hours > 0:
        return (f'{hours} час{h_end} {minutes} минут{m_end}')
    
    return (f'{minutes} минут{m_end}')
